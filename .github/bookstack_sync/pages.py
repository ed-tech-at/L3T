import bookstack
import logging
import requests

import utilities
import setup


# Update page
def update_page(page_id, chapter_id, name, markdown, priority):
	return {
		"id": page_id, 
		"chapter_id": chapter_id, 
		"name": name, 
		"markdown": markdown,
		"priority": priority
	}


# Create page
def create_page(chapter_id, name, markdown, priority):
	return {
		"chapter_id": chapter_id, 
		"name": name, 
		"markdown": markdown,
		"priority": priority
	}


# Process pages to create or update them within a chapter
def upsert_page(chapter_id, metadata, markdown_repo, existing_pages, file_path, book_slug):
	name_repo = metadata["title"]
	priority = int(metadata.get("priority", "98"))

	# Check if the page exists
	page_match = None
	for page in existing_pages:
		if page["name"] == name_repo or page["markdown"] == markdown_repo:
			page_match = page
			slug = page["slug"]
			break

	if page_match:
		page_id = page_match["id"]
		
		is_literature = name_repo.lower() == "literatur"
		name_changed = page_match.get("name", "") != name_repo
		content_changed = page_match.get("markdown", "").strip() != markdown_repo.strip()
		priority_changed = page_match.get("priority", "") != priority
		
		if name_changed or content_changed or (priority_changed and not is_literature):
			data = update_page(page_id, chapter_id, name_repo, markdown_repo, priority)
			response = utilities.retry_request(setup.api.put_pages_update, data)
			if response:
				slug = response.get("slug")
				logging.info(f"Updated page {name_repo} with ID {page_id}.")
			else:
				logging.error(f"Error updating page {name_repo} with ID {page_id}. Changes have not been synced to Bookstack.")
		else:
			logging.debug(f"No changes found in page {name_repo} with ID {page_id}.")
	else:
		# Create new page
		data = create_page(chapter_id, name_repo, markdown_repo, priority)
		response = utilities.retry_request(setup.api.post_pages_create, data)
		if response:
			page_id = response.get("id")
			slug = response.get("slug")
			logging.info(f"Created page {name_repo} with ID {page_id}.")
		else:
			page_id = None
			logging.warning(f"Error creating page {name_repo}. Consider re-running the script.")
	
	# Check and update for slug
	utilities.update_slug_in_file(file_path, slug, setup.base_url, book_slug, is_chapter=False)

	return page_id


# Get description of a page as markdown
def get_page_desc(page_id):
	page_data = utilities.retry_request(setup.api.get_pages_read, {"id": page_id})
	
	if page_data:
		return page_data.get("markdown", "")
	else:
		logging.warning(f"Error reading details of page {page_id}. Comparing changes will probably fail.")
		return ""


# Delete unmatched pages
def delete_pages(base_url, existing_chapters, matched_page_ids):
	existing_page_ids = {
				page["id"]
				for chapter in existing_chapters
				for page in chapter.get("pages", [])
			}
	unmatched_page_ids = existing_page_ids - matched_page_ids

	for page_id in unmatched_page_ids:
		response = utilities.retry_request(requests.delete, f'{base_url}/api/pages/{page_id}', context=f"deleting page {page_id}", headers=setup.headers)
		if response.status_code == 204:
			logging.info(f"Deleted unmatched page with ID {page_id}")
		else:
	 		logging.error(f"Failed to delete page {page_id}: {response.status_code} - {response.text}")
