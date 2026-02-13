import bookstack
import logging
import requests

import utilities
import setup


# Update chapter
def update_chapter(chapter_id, name, description, tags, priority):
	return {
		"id": chapter_id, 
		"name": name, 
		"description_html": description,
		"tags": tags,
		"priority": priority
	}


# Create chapter
def create_chapter(book_id, name, description, tags, priority):
	return {
		"book_id": book_id, 
		"name": name, 
		"description_html": description,
		"tags": tags,
		"priority": priority
	}


# Process chapters to create or update them within the book
def upsert_chapter(book_id, metadata, body, existing_chapters, file_path, book_slug):
	name_repo = metadata["title"]
	tags = [{"name": tag.strip().lstrip('#'), "value": "", "order": 0} for tag in metadata["tags"].split(",")]
	authors = [author.strip() for author in metadata["authors"].split(",")]
	revisors = [revisor.strip() for revisor in metadata.get("revisors", "").split(",")]
	description_repo = utilities.convert_chapter_desc(body, authors, revisors)
	priority = int(metadata.get("priority", "98"))

	# Check if the chapter already exists
	chapter_match = None
	for chapter in existing_chapters:
		if chapter["name"] == name_repo or chapter["description_html"] == description_repo:
			chapter_match = chapter
			slug = chapter["slug"]
			break

	if chapter_match:
		chapter_id = chapter_match["id"]
		
		name_changed = chapter_match.get("name", "") != name_repo
		content_changed = chapter_match.get("description_html", "") != description_repo
		priority_changed = chapter_match.get("priority", "") != priority
		tags_changed = chapter_match.get("tags", "") != tags
		
		# Check for differences in content
		if name_changed or content_changed or priority_changed or tags_changed:
			data = update_chapter(chapter_id, name_repo, description_repo, tags, priority)
			response = utilities.retry_request(setup.api.put_chapters_update, data)
			if response:
				slug = response.get("slug")
				logging.info(f"Updated chapter {name_repo} with ID {chapter_id}.")
			else:
				logging.error(f"Error updating chapter {name_repo} with ID {chapter_id}. Changes have not been synced to Bookstack.")
		else:
			logging.debug(f"No changes found in chapter {name_repo} with ID {chapter_id}.")
	else:
		# Create new chapter
		data = create_chapter(book_id, name_repo, description_repo, tags, priority)
		response = utilities.retry_request(setup.api.post_chapters_create, data)
		if response:
			chapter_id = response.get("id")
			slug = response.get("slug")
			logging.info(f"Created chapter {name_repo} with ID {chapter_id}.")
		else:
			chapter_id = None
			logging.error(f"Error creating chapter {name_repo}. Consider re-running the script.")

	# Check & update slug in file
	utilities.update_slug_in_file(file_path, slug, setup.base_url, book_slug, is_chapter=True)

	return chapter_id


# Get description of a chapter
def get_chap_data(chapter_id):
	chapter_data = utilities.retry_request(setup.api.get_chapters_read, {"id": chapter_id})
	
	if chapter_data:
		return chapter_data
	else:
		logging.warning(f"Error reading details of chapter {chapter_id}. Comparing changes will probably fail.")
		return {"description_html": "", "tags": []}


# Delete unmatched chapters
def delete_chapters(base_url, existing_chapters, matched_chapter_ids, matched_page_ids):
	existing_chapter_ids = {chapter["id"] for chapter in existing_chapters}
	unmatched_chapter_ids = existing_chapter_ids - matched_chapter_ids
	
	for chapter_id in unmatched_chapter_ids:
		chapter = next((c for c in existing_chapters if c["id"] == chapter_id), None)
		if chapter:
			pages = {page["id"] for page in chapter.get("pages", [])}
		
		# Track page_ids of deleted chapter to not delete non existent pages 
		matched_page_ids.update(pages)
	
		response = utilities.retry_request(requests.delete, f'{base_url}/api/chapters/{chapter_id}', context=f"deleting chapter {chapter_id}", headers=setup.headers)
		if response.status_code == 204:
			logging.info(f"Deleted unmatched chapter with ID {chapter_id} and all its subpages")
		else:
			logging.error(f"Failed to delete chapter {chapter_id}: {response.status_code} - {response.text}")


