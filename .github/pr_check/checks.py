import re
from bs4 import BeautifulSoup
from collections import Counter

# Local imports
from logger import error, warning
from utilities import normalize_title, parse_metadata, get_md_files

# Constants
REPO_OWNER = 'ed-tech-at'
REPO_NAME = 'L3T'
ALLOWED_IMAGE_TYPES = {'.png', '.jpg', '.jpeg', '.gif', '.svg', '.webp'}
ALLOWED_FILE_EXTENSIONS = {'.md'}
ALLOWED_CHAPTER_FOLDERS = {'img'}
BLOCKQUOTE_STYLES = {
    'info': {'bg': '#B3E5FC', 'border': '#039BE5', 'heading': '!'},
    'question': {'bg': '#FFEBEE', 'border': '#F44336', 'heading': '?'},
    'practice': {'bg': '#E8F5E9', 'border': '#4CAF50', 'heading': 'In der Praxis'}
}
PUBLICATION_STATUS_PHRASES = ['im Druck', 'eingereicht', 'unveröffentlicht', 'im Erscheine', 'o. J.', 'ohne Jahr']


# Helper to safely read file content
def _read_file(path):
    try:
        return path.read_text(encoding='utf-8')
    except Exception as e:
        error(str(path), f"Datei kann nicht gelesen werden: {e}")
        return None


# Helper function to check for mismatched emphasis markers
def _check_emphasis_balance(line, marker):
    if marker not in line:
        return []
    
    mismatches = []
    # Pattern matches: (marker{1,3})(content)(marker{1,3})
    pattern = rf'({re.escape(marker)}{{1,3}})([^{re.escape(marker)}]+?)({re.escape(marker)}{{1,3}})'
    matches = list(re.finditer(pattern, line))
    
    for m in matches:
        opening = m.group(1)
        closing = m.group(3)
        if len(opening) != len(closing):
            mismatches.append(m.group(0))
    
    return mismatches


# Check basic metadata presence and validity
def file_metadata(path):
    text = _read_file(path)
    if text is None:
        return {}
    
    meta, counts = parse_metadata(text)
    
    # Duplicate keys
    for key, count in counts.items():
        if count > 1:
            error(str(path), f"Metadaten doppelt vorhanden: '{key}'")
    
    # Required: filename
    if not meta.get('filename'):
        error(str(path), "Fehlende Metadaten 'filename'")
    elif meta['filename'] != path.name:
        error(str(path), f"Metadaten-Dateiname '{meta['filename']}' ≠ tatsächlicher Name '{path.name}'")
    
    # Required: title
    title = meta.get('title')
    if not title:
        error(str(path), "Fehlende Metadaten 'title'")
    else:
        # Check title matches filename
        expected = normalize_title(title)
        actual = normalize_title(re.sub(r'^\d+[-_]+', '', path.stem))
        if expected.lower() != actual.lower():
            warning(str(path), f"Titel ist '{title}' → '{expected}' aber Datei ist '{actual}'")
    
    return meta


# Check chapter-specific metadata
def chapter_metadata(path, meta):
    # Authors required
    if not meta.get('authors'):
        error(str(path), "Keine Autoren in den Metadaten gefunden")
    else:
        authors = [a.strip() for a in meta['authors'].split(',') if a.strip()]
        if not authors:
            error(str(path), "Autoren-Tag vorhanden, aber keine gültigen Namen gefunden")
    
    # Revisors (optional, validate format if present)
    if meta.get('revisors'):
        revisors = [r.strip() for r in meta['revisors'].split(',') if r.strip()]
        if not revisors:
            warning(str(path), "Revisoren in den Metadaten vorhanden aber leer/fehlerhaft")
    
    # Tags (optional, recommended)
    if not meta.get('tags'):
        warning(str(path), "Keine Tags in den Metadaten gefunden (empfohlen)")
    else:
        for tag in meta['tags'].split(','):
            if tag.strip() and not tag.strip().startswith('#'):
                error(str(path), f"Tag '{tag.strip()}' muss mit # beginnen")


# Check page-specific metadata and doesn't have chapter-only metadata
def page_metadata(path, meta):
    for key in ('tags', 'authors', 'revisors'):
        if meta.get(key):
            error(str(path), f"'{key}' nicht erlaubt in Seiten eines Kapitels")


# Check content of chapter file
def chapter_content(path):
    text = _read_file(path)
    if text is None:
        return
    
    lines = text.splitlines()
    
    # Skip metadata comments and blank lines
    i = 0
    while i < len(lines):
        line = lines[i]
        stripped = line.strip()
        if not stripped:      # Skip blank lines
            i += 1
            continue
        if '<!--' in line:          # Skip comment block
            while i < len(lines) and '-->' not in lines[i]:
                i += 1
            i += 1
            continue
        break
    
    # Must start with subtitle (## ...)
    first_line = lines[i].strip()
    if not re.match(r'^#{2}\s+.+', first_line):
        error(str(path), f"Muss mit ## Untertitel beginnen, gefunden: {first_line}")
        return
    
    i += 1
    
    # Check rest
    while i < len(lines):
        line = lines[i]
        stripped = line.strip()
        if not stripped:                # Skip blank lines
            i += 1
            continue
        
        if re.match(r'^\s*#{1,6}\s+', line):
            error(str(path), f"Keine weiteren Überschriften nach Untertitel erlaubt: {stripped}")
            return
        found_error = False
        
        if re.search(r'\[.+?\]\(.+?\)', line):  # Links
            error(str(path), f"Links nicht erlaubt in Kapiteldatei: {stripped}")
            found_error = True
        
        if re.search(r'<[a-zA-Z/][^>]*>', line):  # HTML tags
            error(str(path), f"HTML-Tags nicht erlaubt in Kapiteldatei: {stripped}")
            found_error = True
        
        if line.count('|') >= 2 and re.search(r'\|[^|]+\|', line):  # Tables
            error(str(path), f"Tabellen nicht erlaubt in Kapiteldatei: {stripped}")
            found_error = True
        
        if found_error:
            return
        
        i += 1


# Check for correct markdown formatting in all files
def content(path):
    text = _read_file(path)
    if text is None:
        return
    
    # Check for completely empty content beyond metadata
    lines_no_meta = [l for l in text.split('\n') if l.strip() and not l.strip().startswith('<!--')]
    if len(lines_no_meta) == 0:
        error(str(path), "Datei ist leer (kein Inhalt nach Metadaten)")

    
    # Check for bad image paths - must use GitHub raw URLs with correct repo structure
    expected_base = f'https://raw.githubusercontent.com/{REPO_OWNER}/{REPO_NAME}/refs/heads/main'
    if re.search(rf'src=["\'](?!{re.escape(expected_base)})[^"\']*?/img/', text):
        error(str(path), f"Bilder müssen korrekte GitHub raw URLs verwenden ({expected_base}/...)")
    
    # Check figures-syntax
    for m in re.finditer(r'<figure>.*?</figure>', text, re.DOTALL | re.I):
        soup = BeautifulSoup(m.group(0), 'html.parser')
        fig = soup.find('figure')
        if not fig:
            continue
        
        # Check if <figure> is wrapped in <center>
        match_start = m.start()
        match_end = m.end()

        before = text[max(0, match_start-50):match_start]
        after = text[match_end:min(len(text), match_end+50)]
        
        if not (re.search(r'<center\s*>', before, re.I) and re.search(r'</center\s*>', after, re.I)):
            error(str(path), "figure-Element muss in center-Element eingebettet sein")
            continue
        
        # Must have img
        img_tag = fig.find('img')
        if not img_tag:
            error(str(path), "figure-Element fehlt img-Tag")
            continue
        
        # Must have figcaption
        figcaption = fig.find('figcaption')
        if not figcaption:
            error(str(path), "figure-Element fehlt figcaption-Element")
        
        # Must have alt attribute
        alt = img_tag.get('alt', '').strip()
        if not alt:
            warning(str(path), "img-Element fehlt 'alt'-Attribut")
        
        # Check alt and figcaption match
        if figcaption:
            caption_text = figcaption.get_text().strip()
            if caption_text and alt and caption_text != alt:
                warning(str(path), f"Abbildung-'alt'-Attribut '{alt}' stimmt nicht mit figcaption-Text '{caption_text}' überein")
    
    # Blockquotes style validation
    for m in re.finditer(r'(<blockquote\s+[^>]*>.*?</blockquote>)', text, re.DOTALL | re.I):
        soup = BeautifulSoup(m.group(1), 'html.parser')
        bq = soup.find('blockquote')
        if not bq:
            continue
        
        style = bq.get('style', '').lower()
        
        # Must have 10x border-left
        if 'border-left' not in style or '10px' not in style:
            error(str(path), "blockquote benötigt 'border-left: 10px solid ...'")
            continue
        
        # Check for valid color scheme
        valid_scheme = False
        matched_scheme = None
        for scheme_name, colors in BLOCKQUOTE_STYLES.items():
            if colors['bg'].lower() in style and colors['border'].lower() in style:
                valid_scheme = True
                matched_scheme = (scheme_name, colors)
                break
        
        if not valid_scheme:
            error(str(path), f"Blockquote verwendet nicht-standardisierte Farben (soll im jeweiligen Schema (!/?/In der Praxis) sein - siehe Readme)")
        else:
            # Check if heading matches the color scheme
            scheme_name, colors = matched_scheme
            bq_text = bq.get_text().strip()
            expected_heading = colors['heading']
            
            h3_match = re.search(r'^###\s+(.+?)$', bq_text, re.MULTILINE)
            if h3_match:
                actual_heading = h3_match.group(1).strip()
                # Check if actual heading matches expected
                if expected_heading not in actual_heading:
                    error(str(path), f"Blockquote mit {scheme_name} Farben soll '### {expected_heading}' Überschrift haben, gefunden: '### {actual_heading}'")
    
    # Check heading hierarchy
    headings = re.findall(r'^(#{1,6})\s+', text, re.MULTILINE)
    for i in range(1, len(headings)):
        prev_level = len(headings[i-1])
        curr_level = len(headings[i])
        if curr_level > prev_level + 1:
            warning(str(path), f"Überschriftenhierarchie übersprungen (#{prev_level} zu #{curr_level})")
    
    # Markdown link validation
    for m in re.finditer(r'\[([^\]]+)\]\(([^)]*)\)', text):
        link_text = m.group(1)
        link_url = m.group(2).strip()
        
        # Check for empty links
        if not link_url:
            error(str(path), f"Leerer Link gefunden - Text: '{link_text}', URL: (leer)")
            continue
        
        # Skip special links
        if link_url.startswith(('#', 'mailto:', 'tel:')):
            continue
        
        # Check if it's an external URL (not a relative path)
        if '://' in link_url:
            if not link_url.startswith(('http://', 'https://')):
                warning(str(path), f"Link verwendet unübliches Protokoll - Text: '{link_text}', URL: '{link_url}' (empfohlen: http:// oder https://)")
            
            # Check for basic URL structure
            domain_match = re.match(r'https?://([^/\s]+)', link_url)
            if domain_match:
                domain = domain_match.group(1).rstrip('.')  # Remove trailing dots
                # Remove port if present
                domain_without_port = domain.split(':')[0]
                # Check for at least one dot - TLD-check
                if '.' not in domain_without_port:
                    error(str(path), f"Link scheint keine gültige Domain zu haben (TLD fehlt?) - Text: '{link_text}', URL: '{link_url}'")
    
    # Check for links with unclosed parentheses at end of line
    for m in re.finditer(r'\[([^\]]+)\]\(([^)\n]*)$', text, re.MULTILINE):
        link_text = m.group(1)
        partial_url = m.group(2).strip()
        if partial_url:
            error(str(path), f"Unvollständiger Markdown-Link (schließende Klammer fehlt) - Text: '{link_text}', URL beginnt mit: '{partial_url}'")
        else:
            error(str(path), f"Unvollständiger Markdown-Link (schließende Klammer fehlt) - Text: '{link_text}', URL: (leer)")
    
    # Basic table validation and emphasis balance check
    lines = text.split('\n')
    in_table = False
    table_col_count = None
    for i, line in enumerate(lines):
        # Table validation
        if '|' in line and line.strip():
            cols = line.count('|')
            if not in_table:
                in_table = True
                table_col_count = cols
            else:
                # Check consistent column count
                if cols != table_col_count:
                    # Allow separator row (|---|---|---|) to have different format
                    if not re.match(r'^\s*\|?[\s:-]+\|[\s|:-]+\|?\s*$', line):
                        warning(str(path), f"Tabellenspaltenanzahl stimmt nicht überein in Zeile {i+1}")
        elif in_table and line.strip() == '':
            in_table = False
            table_col_count = None
        
        # Check for mismatched emphasis markers (*, _)
        line_without_links = re.sub(r'\[([^\]]+)\]\(([^)]+)\)', '', line)    # Remove markdown links
        line_without_links = re.sub(r'<[^>]+>', '', line_without_links)      # Remove HTML tags
        for marker in ('*', '_'):
            mismatches = _check_emphasis_balance(line_without_links, marker)
            for mismatch in mismatches:
                error(str(path), f"Ungleiche Hervorhebungs-Marker gefunden (Zeile {i+1}): {mismatch}")


# Check images in chapter for allowed types and usage
def images(chapter_path):
    img_dir = chapter_path / 'img'
    
    # Read all markdown content in this chapter
    all_content = '\n'.join(filter(None, (_read_file(md) for md in get_md_files(chapter_path))))
    
    # Extract all image references from text
    referenced_images = set()
    for match in re.finditer(r'<img[^>]+src=["\']([^"\']+)["\']', all_content, re.I):
        url = match.group(1)
        # Extract filename from Github-Raw-URL
        img_filename = url.split('/')[-1] if '/' in url else url
        referenced_images.add(img_filename)
    
    # Skip check if img/ doesn't exist or empty
    if not img_dir.exists() or not any(img_dir.iterdir()):
        # Warn if images are referenced but folder doesn't exist
        if referenced_images:
            warning(str(chapter_path), f"Bilder im Text referenziert, aber img/ Ordner fehlt oder ist leer: {', '.join(sorted(referenced_images))}")
        return
    
    existing_images = set()
    for img in img_dir.iterdir():
        if img.is_file():
            existing_images.add(img.name)
            if img.suffix.lower() not in ALLOWED_IMAGE_TYPES:
                error(str(img), f"Nicht erlaubter Bildtyp: {img.suffix} (erlaubt: {', '.join(ALLOWED_IMAGE_TYPES)})")
            
            # Check if image is referenced in text
            if img.name not in referenced_images:
                warning(str(img), f"Ungenutztes Bild: {img.name}")
    
    # Check for referenced images that don't exist in folder
    missing_images = referenced_images - existing_images
    for missing in missing_images:
        warning(str(chapter_path), f"Bild im Text referenziert, aber nicht im img/ Ordner vorhanden: {missing}")


# Check chapter has only expected files and folders
def chapter_structure(chapter_path):
    # Check for mandatory chapter file (00_*.md)
    chapter_name = chapter_path.name.split('_', 1)[1] if '_' in chapter_path.name else chapter_path.name
    chapter_file = chapter_path / f"00_{chapter_name}.md"
    if not chapter_file.exists():
        error(str(chapter_path), f"Fehlende Kapiteldatei: 00_{chapter_name}.md bzw. Kapitelname ≠ Kapiteldatei")
    
    for item in chapter_path.iterdir():
        if item.is_file():
            if item.suffix.lower() not in ALLOWED_FILE_EXTENSIONS:
                error(str(item), f"Unerwarteter Dateityp (nur folgende Dateiendungen erlaubt: {', '.join(ALLOWED_FILE_EXTENSIONS)} )")
            # Check filename format
            if not re.match(r'^\d{2}_.*\.md$', item.name):
                error(str(item), "Datei muss dem Format 'NN_Name.md' folgen (2-stellige fortlaufende Nummer, Unterstrich, Name)")
        elif item.is_dir():
            if item.name not in ALLOWED_CHAPTER_FOLDERS:
                error(str(item), f"Unerwarteter Ordner (nur folgende Ordner erlaubt: {', '.join(ALLOWED_CHAPTER_FOLDERS)})")
        else:
            warning(str(item), f"Unerwarteter Elementtyp")


# Check figure numbering across all files within one chapter
def figure_numbering(chapter_path):
    files = get_md_files(chapter_path)
    
    # Collect all figure numbers using <figcaption>
    fig_occurrences = {}
    for f in files:
        text = _read_file(f)
        if text:
            for m in re.finditer(r'<figcaption>.*?Abb\.\s*(\d+).*?</figcaption>', text, re.DOTALL | re.I):
                fig_num = int(m.group(1))
                fig_occurrences.setdefault(fig_num, []).append(f.name)
    
    if fig_occurrences:
        all_fig_nums = sorted(fig_occurrences.keys())
        
        # Check for gaps in numbering and starting from 1
        expected = list(range(1, len(all_fig_nums) + 1))
        if all_fig_nums != expected:
            warning(str(chapter_path), f"Nummerierungen von Abbildungen nicht fortlaufend: erwartet {expected}, gefunden {all_fig_nums}")
        
        # Check for duplicates 
        for fig_num, file_list in fig_occurrences.items():
            if len(file_list) > 1:
                warning(str(chapter_path), f"Abb. {fig_num} erscheint mehrfach: {', '.join(file_list)}")


# Check page numbering and literature file presence
def numbering(chapter_path):
    files = get_md_files(chapter_path)
    
    nums = []
    for f in files:
        m = re.match(r'^(\d{2})_', f.name)
        if m:
            nums.append(int(m.group(1)))
    
    nums_no99 = [n for n in nums if n != 99]
    
    # Duplicate numbers
    counts = Counter(nums_no99)
    dups = [n for n, count in counts.items() if count > 1]
    if dups:
        warning(str(chapter_path), f"Mehrfache Verwendung der gleichen Nummerierung: {dups}")
    elif nums_no99:
        # Gaps in numbering
        missing = [i for i in range(nums_no99[0], nums_no99[-1] + 1) if i not in nums_no99]
        if missing:
            warning(str(chapter_path), f"Nummerierung von Dateien sollte fortlaufend sein, Nummer ausgelassen: {missing}")
    
    # Literature-file check
    literature = [f for f in files if f.name == '99_Literatur.md']
    if len(literature) > 1:
        warning(str(chapter_path), "Mehrere Literatur-Dateien gefunden")    # Should not be possible
    elif not literature and chapter_path.name != '01_Einleitung':           # Chapter "Einleitung" omits literature file
        warning(str(chapter_path), "Keine Literatur-Datei (99_Literatur.md) gefunden")


# Basic check of literature file for APA formatting and citation usage
def literature_file(lit_path, chapter_path):
    text = _read_file(lit_path)
    if text is None:
        return
    
    lines = text.splitlines()
    
    # Check if file is empty or very short
    content_lines = [l for l in lines if l.strip() and not l.strip().startswith(('#', '<!--'))]
    if len(content_lines) < 3:
        warning(str(lit_path), "Literaturdatei erscheint leer oder sehr kurz")
        return
    
    # Build regex pattern from publication status phrases
    pub_status_pattern = '|'.join(re.escape(phrase) for phrase in PUBLICATION_STATUS_PHRASES)
    
    # Track date formats used in this file for consistency check
    date_formats_used = set()
    
    for i, line in enumerate(lines, 1):
        stripped = line.strip()
        # Skip empty lines, headings, and comments
        if not stripped or stripped.startswith(('#', '<!--')):
            continue
        
        # Remove markdown list markers
        if stripped.startswith(('- ', '* ')):
            stripped = stripped[2:].strip()
        
        # Exception for legal sources and general webpages (skips year requirement if URL present and no author)
        has_url = 'URL:' in stripped or re.search(r'https?://', stripped)
        has_author_format = re.match(r'^[A-ZÄÖÜ][a-zäöüß-]+,\s+[A-ZÄÖÜ]', stripped)
        
        if has_url and not has_author_format:
            # Legal source or organizational document without year - skip validation
            continue
        
        # Check for year or publication status (accepting (YYYY), (YYYY/YYYY), or publication status phrases)
        year_match = re.search(r'\((\d{4}[a-z]?(?:/\d{4}[a-z]?)?)\)', stripped)
        status_match = re.search(rf'\(({pub_status_pattern})\)', stripped, re.IGNORECASE)
        
        if not year_match and not status_match:
            warning(str(lit_path), f"Zeile {i}: Referenz fehlt Jahr/Publikationsstatus oder ist im falschen Format, korrekt: (YYYY)")
            continue
        
        if year_match:
            year = year_match.group(1)
            date_pattern = r'\(\d{4}[a-z]?(?:/\d{4}[a-z]?)?\)'
        elif status_match:
            year = status_match.group(1)
            date_pattern = rf'\(({pub_status_pattern})\)'
        
        # Check for period after year/status
        if re.search(date_pattern + r'\s+[A-ZÄÖÜ]', stripped, re.IGNORECASE):  # True if no period found
            warning(str(lit_path), f"Zeile {i}: Punkt nach Jahr/Status fehlt")
        
        # Check URL format and access date if present
        if has_url:
            # Check URL format (URL: ...)
            if 'url:' in stripped.lower():
                url_match = re.search(r'URL:\s*([^\s\[]+)', stripped, re.I)
                if url_match:
                    url = url_match.group(1)
                    if not url.startswith(('http://', 'https://')):
                        warning(str(lit_path), f"Zeile {i}: Ungültiges URL-Format (sollte mit http:// oder https:// beginnen)")
            
            # Check for access date when URL is present - accept both formats
            # Accepts [YYYY-MM-DD] or [DD.MM.YYYY] or [D.M.YYYY]
            iso_date = re.search(r'\[(\d{4}-\d{2}-\d{2})\]', stripped)
            eu_date = re.search(r'\[(\d{1,2}\.\d{1,2}\.\d{4})\]', stripped)
            
            if iso_date:
                date_formats_used.add('ISO')
            elif eu_date:
                date_formats_used.add('EU')
            else:
                warning(str(lit_path), f"Zeile {i}: URL vorhanden, aber Zugriffsdatum fehlt oder ist in falschem Format ([YYYY-MM-DD] oder [DD.MM.YYYY])")
        
        # Check for period at end of citation
        if not stripped.endswith('.'):
            warning(str(lit_path), f"Zeile {i}: Referenz sollte mit einem Punkt enden")
    
    # Warn if mixed date formats within one file
    if len(date_formats_used) > 1:
        warning(str(lit_path), f"Gemischte Datumsformate innerhalb einer Datei: {', '.join(sorted(date_formats_used))} - empfohlen wird einheitliches Format")


# Check duplicate slugs across all markdown files
def slugs(workspace):
    # Exclude README.md and .git folders
    md_files = [p for p in workspace.rglob('*.md') 
                if '.git' not in p.parts and p.name.lower() != 'readme.md']
    
    slugs = {'chapter': {}, 'page': {}}
    for p in md_files:
        try:
            text = p.read_text(encoding='utf-8')
            meta, _ = parse_metadata(text)
            slug = meta.get('slug', '').strip()
            url = meta.get('url', '').strip()
            
            # Determine file type
            is_chapter = p.name.startswith('00_')
            is_book_desc = is_chapter and '00_' in p.parent.name      # Skip book description
            
            # Skip files without slug
            if not slug:
                continue
            
            # Track slugs for duplicate detection
            file_type = 'chapter' if is_chapter else 'page'
            slugs[file_type].setdefault(slug, []).append(str(p))
            
            # Check consistency of slug and URL if both exist
            if url and not is_book_desc:
                expected_content_type = 'chapter' if is_chapter else 'page'
                url_pattern = rf'/{expected_content_type}/(.+?)(?:\?|$)'
                url_match = re.search(url_pattern, url)
                
                if url_match:
                    url_slug = url_match.group(1)
                    if url_slug != slug:
                        warning(str(p), f"Slug '{slug}' und URL-Slug '{url_slug}' stimmen nicht überein (wird durch Sync zu Bookstack korrigiert)")
        
        except Exception:
            # Skip files that can't be parsed
            continue
    
    # Warn about duplicate slugs
    for file_type, slug_map in slugs.items():
        for slug, files in slug_map.items():
            if len(files) > 1:
                warning('.', f"Slug-Kollision '{slug}' in {file_type}: {files} (wird durch Sync zu Bookstack korrigiert)")