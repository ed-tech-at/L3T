import bookstack
import re
import logging
import time
from pathlib import Path


# Wrapper for retrying API calls
def retry_request(func, *args, retries=3, delay=1, exception=Exception, context="", **kwargs):
	for attempt in range(retries):
		try:
			return func(*args, **kwargs)
		except exception as e:
			msg = f"Attempt {attempt + 1} failed"
			if context:
				msg += f" while {context}"
			logging.warning(f"{msg}: {e}")
			if attempt < retries - 1:
				time.sleep(delay)
			else:
				logging.error(f"Giving up after {retries} attempts{f' while {context}' if context else ''}.")
	return None


# Check slugs from Bookstack and update on backend if necessary
def update_slug_in_file(filepath: Path, slug_str: str, base_url: str = None, book_slug: str = None, is_chapter: bool = None):
    with open(filepath, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    # Regular expressions for finding existing comments
    url_re = re.compile(r'<!--\s*URL:\s*(.*?)\s*-->')
    slug_re = re.compile(r'<!--\s*slug:\s*(.*?)\s*-->')

    existing_url_idx = None
    existing_slug_idx = None

    # Find existing URL and slug comments
    for i, line in enumerate(lines):
        if url_re.match(line):
            existing_url_idx = i
        if slug_re.match(line):
            existing_slug_idx = i

    # Build URL if file is page or chapter
    url_comment = None
    if base_url is not None and book_slug is not None and is_chapter is not None:
        content_type = "chapter" if is_chapter else "page"
        url = f"{base_url}/books/{book_slug}/{content_type}/{slug_str}"
        url_comment = f"<!-- URL: {url} -->\n"

    slug_comment = f"<!-- slug: {slug_str} -->\n"

    # Remove existing URL and slug comments
    indices_to_remove = []
    if existing_url_idx is not None:
        indices_to_remove.append(existing_url_idx)
    if existing_slug_idx is not None:
        indices_to_remove.append(existing_slug_idx)
    
    # Remove in reverse order to maintain indices
    for idx in sorted(indices_to_remove, reverse=True):
        del lines[idx]

    # Insert URL and slug comments at the beginning of the file
    if url_comment:
        lines.insert(0, slug_comment)
        lines.insert(0, url_comment)
        logging.debug(f"URL and slug updated: {url_comment.strip()}")
    else:
        # For book description files, only insert slug
        lines.insert(0, slug_comment)
        logging.debug(f"Slug updated: {slug_str}")

    with open(filepath, 'w', encoding='utf-8') as f:
        f.writelines(lines)


# Convert chapter descriptions to HTML
def convert_chapter_desc(text, authors, revisors):
    # convert level-2 headings to strong
    text = re.sub(r'^##\s*(.*)', r'<strong>\1</strong>', text, flags=re.MULTILINE)

    # convert bold+italic, bold, and italic markdown to HTML
    text = re.sub(r'(?s)(\*\*\*|___)(.+?)\1', r'<strong><em>\2</em></strong>', text)
    text = re.sub(r'(?s)(\*\*|__)(.+?)\1', r'<strong>\2</strong>', text)
    text = re.sub(r'(?s)(\*|_)(.+?)\1', r'<em>\2</em>', text)

    lines = text.splitlines()
    processed_lines = []
    for line in lines:
        if not line.strip():
            continue  # skip empty lines
        if line.startswith("<strong>"):
            processed_lines.append(line + "<p></p>")
        else:
            processed_lines.append(f"<p>{line}</p>")

    author_text = "Autor" if len(authors) == 1 else "Autoren"
    if revisors and revisors[0].strip() != '':
        authors_revisors = f"<em>{author_text}: {', '.join(authors)}</em><br /> <em>Überarbeitet von: {', '.join(revisors)}</em>"
    else:
        authors_revisors = f"<em>{author_text}: {', '.join(authors)}</em>"

    return "".join(processed_lines + [authors_revisors])


# Extract metadata from file
def extract_metadata(file_path, priority, is_chapter):
	with open(file_path, 'r', encoding='utf-8') as file:
		content = file.readlines()

	metadata = {}
	body = ""
	content_start = 0
	for i, line in enumerate(content):
		if line.startswith("<!--"):
			match = re.match(r"<!--\s*(.*?):\s*(.*)\s*-->", line.strip())
			if match:
				key, value = match.groups()
				metadata[key.strip()] = value.strip()
		elif line.startswith("##") and is_chapter:
			content_start = i
		elif line.startswith("<p>") and is_chapter:
			content_start = i
			body = ''.join(content[content_start:])
			break
		else:
			body = ''.join(content[content_start:])
	
	#add priority to dictionary
	metadata["priority"] = priority
	
	return metadata, body


# Extract priority from file or folder name
def extract_priority(name):
	match = re.match(r"^(\d+)_", name)
	if match:
		return int(match.group(1))
	return 98 # Fallback priority


# Replace certain occurrences in Dictionary with a new sequence (e.g. &amp; with &)
def replace_sequence_in_dict(obj, org_sequence, replacement):
	if isinstance(obj, dict):
		return {key: replace_sequence_in_dict(value, org_sequence, replacement) for key, value in obj.items()}
	elif isinstance(obj, list):
		return [replace_sequence_in_dict(item, org_sequence, replacement) for item in obj]
	elif isinstance(obj, str):
		return obj.replace(org_sequence, replacement)
	else:
		return obj