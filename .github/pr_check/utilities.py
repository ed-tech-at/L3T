import re
from unidecode import unidecode

# German character normalization for proper transliteration
# (unidecode would convert ä→a, but we want ä→ae for German)
GERMAN_CHARS = str.maketrans({
    'Ä': 'Ae', 'Ö': 'Oe', 'Ü': 'Ue',
    'ä': 'ae', 'ö': 'oe', 'ü': 'ue', 'ß': 'ss',
    '&': 'und', '–': '-', '—': '-', '/': '-'
})


# Normalize title to expected filename format
def normalize_title(title):
    s = title.strip()
    # Extract from brackets if present
    m = re.search(r'\[([^\]]+)\]', s)
    if m:
        s = m.group(1)
    
    s = s.translate(GERMAN_CHARS)                               # German-specific transliteration
    s = re.sub(r'[^\w\s-]', '', s)                              # Remove special characters (keep word chars, spaces, hyphens)
    s = re.sub(r'[-\s_]+', '_', s)                              # Replace spaces/hyphens/underscores with single underscore
    s = re.sub(r'_+', '_', s).strip('_')                        # Consolidate underscores and trim
    return unidecode(s)                                         # Remove any remaining accents


# Parse metadata from HTML comments
def parse_metadata(text):
    meta = {}
    counts = {}
    for line in text.splitlines()[:20]: # Only scan first 20 lines
        m = re.match(r'^\s*<!--\s*(\w+)\s*:\s*(.*?)\s*-->\s*$', line, re.I)
        if m:
            key, value = m.group(1).strip().lower(), m.group(2).strip()
            counts[key] = counts.get(key, 0) + 1
            if key not in meta:
                meta[key] = value
    return meta, counts


# Helper to get sorted markdown files from directory
def get_md_files(directory):
    return sorted([f for f in directory.iterdir() if f.is_file() and f.suffix.lower() == '.md'])
