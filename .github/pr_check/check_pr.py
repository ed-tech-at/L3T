#!/usr/bin/env python3

import re
import argparse
from pathlib import Path

# Local imports
import checks
from logger import actions_summary, console_summary
from utilities import get_md_files

def main():
    parser = argparse.ArgumentParser(description='Führt PR-Checks für das L3T-Repository durch')
    parser.add_argument('-c', '--chapters', type=str, help='Kapitelnummern welche zu prüfen sind (getrennt durch Komma, Semikolon oder Leerzeichen, z.B. "1,2,5,26")')
    args = parser.parse_args()
    
    workspace = Path.cwd()
    
    # Parse chapter filter
    chapter_filter = None
    if args.chapters:
        # Convert chapter numbers to set
        try:
            # Split on comma, semicolon, space, or any combination
            chapter_numbers = set(int(num) for num in re.split(r'[,;\s]+', args.chapters) if num.strip())
            chapter_filter = chapter_numbers
            print(f"Prüfe Kapitel mit den Nummern {', '.join(str(n) for n in sorted(chapter_filter))}")
        except ValueError:
            print(f"Warnung: Ungültiges Format für Kapitelnummern: {args.chapters}")
            print("Vollständige Prüfung aller Kapitel")
    else:
        print("Vollständige Prüfung aller Kapitel")
    
    print("Führe PR-Überprüfungen durch...")
    
    # Slugs check - always runs globally on all chapters
    checks.slugs(workspace)
    
    # Process chapters
    chapters = []
    for entry in sorted(workspace.iterdir()):
        if entry.is_dir() and re.match(r'^\d{2}_', entry.name) and not entry.name.startswith('00_'):
            chapters.append(entry)
    
    # Apply chapter filter if specified
    if chapter_filter:
        # Match chapter numbers to folder names (e.g., 1 → "01_Einleitung")
        filtered_chapters = []
        for chapter in chapters:
            match = re.match(r'^(\d+)_', chapter.name)      # Extract chapter number from folder name
            if match:
                chapter_num = int(match.group(1))
                if chapter_num in chapter_filter:
                    filtered_chapters.append(chapter)
        
        chapters = filtered_chapters
        if not chapters:
            print(f"Warnung: Keine passenden Kapitel für folgende Nummern gefunden: {chapter_filter}")
        else:
            print(f"Prüfe {len(chapters)} Kapitel: {', '.join(c.name for c in chapters)}")
    else:
        print(f"Prüfe alle {len(chapters)} Kapitel")
    
    # Scan all markdown files in chapters
    for entry in chapters:
        checks.chapter_structure(entry)
        checks.numbering(entry)
        checks.figure_numbering(entry)
        
        # Check literature file if it exists
        lit_file = entry / '99_Literatur.md'
        if lit_file.exists():
            checks.literature_file(lit_file, entry)
        
        for md in get_md_files(entry):
            is_chapter = md.name.startswith('00_')
            
            # Check Metadata and content of markdown files
            meta = checks.file_metadata(md)
            if is_chapter:
                checks.chapter_metadata(md, meta)
                checks.chapter_content(md)
            else:
                checks.page_metadata(md, meta)
            
            checks.content(md)
    
    # Check for unused images in chapters
    for entry in chapters:
        checks.images(entry)
    
    # Write summary
    actions_summary()
    return console_summary()


if __name__ == "__main__":
    raise SystemExit(main())
