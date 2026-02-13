import bookstack
import requests
import os
import re
import logging
from glob import glob
import sys

# Local files
import setup
import chapters
import pages
import utilities


# Process all chapters and pages of a certain book
def check_chapters_pages(book_id, book_slug, existing_chapters):
	matched_chapter_ids = set()
	matched_page_ids = set()
	for folder_name in sorted(os.listdir()):
		if folder_name.startswith("00_") or not os.path.isdir(folder_name):
			continue
	
		chapter_id = None
	
		for file_name in sorted(os.listdir(folder_name)):
			file_path = os.path.join(folder_name, file_name)

			if file_name.endswith(".md"):
				if file_name.startswith("00_"):
					priority = utilities.extract_priority(folder_name)
					metadata, body = utilities.extract_metadata(file_path, priority, True)
					chapter_id = chapters.upsert_chapter(book_id, metadata, body, existing_chapters, file_path, book_slug)
					if chapter_id != None:
						matched_chapter_ids.add(chapter_id)
						current_chapter = next((c for c in existing_chapters if c["id"] == chapter_id), None)
						if current_chapter:
							existing_pages = current_chapter.get("pages", [])
						else:
							existing_pages = []
							logging.warning(f"No pages found for chapter with ID {chapter_id}")
					else:
						logging.error(f"No chapter ID returend. Furhter sync might fail.")
				elif re.match(r"^\d{2}_", file_name):
					priority = utilities.extract_priority(file_name)
					metadata, body = utilities.extract_metadata(file_path, priority, False)
					if chapter_id != None:
						page_id = pages.upsert_page(chapter_id, metadata, body, existing_pages, file_path, book_slug)
						if page_id != None:
							matched_page_ids.add(page_id)
					else:
						logging.error(f"No chapter ID returend. Furhter sync might fail.")
				else:
					continue
	
	return matched_chapter_ids, matched_page_ids


# Gets all chapters and pages from selected book
def check_bookstack(book_id):
	existing_chapters = []
	existing_chapters_raw = utilities.retry_request(setup.api.get_books_read, {'id': book_id}, context=f"reading content of book {book_id}")
	
	if existing_chapters_raw:
		contents = existing_chapters_raw.get("contents", [])

		for c in contents:
			if c["type"] != "chapter":
				continue
		
			chapter_data = chapters.get_chap_data(c["id"])
			
			current_chapter = {
				"id": c["id"],
				"name": c["name"],
				"priority": c["priority"],
				"slug": c["slug"],
				"description_html": chapter_data.get("description_html", ""),
				"tags": chapter_data.get("tags", []),
				"pages": [
					{
						"id": p["id"],
						"name": p["name"],
						"slug": p["slug"],
						"priority": p["priority"],
						"markdown": pages.get_page_desc(p["id"])
					}
					for p in c.get("pages", [])
				]
			}
			
			existing_chapters.append(current_chapter)
	
		# Some post-processing of content pulled from Bookstack
		existing_chapters = utilities.replace_sequence_in_dict(existing_chapters, "&amp;", "&")
	else:
		logging.critical(f"Failed to retrieve book data for ID {book_id}. Aborting sync.")
		sys.exit(1)
	
	return existing_chapters


# Search for image files in given folder
def get_cover_image(img_folder):
	valid_extensions = (".jpg", ".jpeg", ".png", ".gif", ".webp")
	images = [f for f in glob(os.path.join(img_folder, "*")) if f.lower().endswith(valid_extensions)]
	
	if len(images) == 0:
		logging.critical(f"No image found in {img_folder}. A single front cover image is required.")
		sys.exit(1)
	elif len(images) > 1:
		logging.critical(f"Multiple images found in {img_folder}. Only one cover image should be present.")
		sys.exit(1)
	
	return images[0]


# Check if book exists, create if necessary
def upsert_book():
	base_path, description_file = setup.book_base_path()
	image_folder = os.path.join(base_path, "img")

	book_list = utilities.retry_request(setup.api.get_books_list, context="searching for book on server")
	
	if book_list:
		metadata, body = utilities.extract_metadata(description_file, 1, True)
		
		book = next((b for b in book_list["data"] if b["name"] == metadata['title']), None)
		if book:
			book_id = book['id']
			slug = book['slug']
			logging.debug(f"Book found with ID {book_id}")
		else:
			book_data = {"name": metadata['title'], "description_html": body}
			cover_image = get_cover_image(image_folder)	
			
			with open(cover_image, "rb") as image_file:
				files = {"image": image_file}
				response = utilities.retry_request(requests.post, f'{setup.base_url}/api/books', context="creating book", headers=setup.headers, data=book_data, files=files)
				if response.status_code == 200:
					book_id = response.json()['id']
					slug = response.json()['slug']
					logging.info(f"Book created with ID {book_id}.")
				else:
					logging.critical(f"Error creating book with HTML status code {response.status_code}.")
					sys.exit(1)
	else:
		logging.critical("Failed to retrieve list of books. Aborting sync.")
		sys.exit(1)

	utilities.update_slug_in_file(description_file, slug, setup.base_url)
		
	return book_id, slug


## Initial setup
setup.init()

## Start of synchronisation
logging.info("Starting synchronisation")

# Create or update book
book_id, book_slug = upsert_book()

# Check for current structure on Bookstack
logging.info("Pulling data from Bookstack")
existing_chapters = check_bookstack(book_id)

# Check all chapters and pages for changes and update if necessary
logging.info("Comparing data between Bookstack & Git-Repo")
matched_chapter_ids, matched_page_ids = check_chapters_pages(book_id, book_slug, existing_chapters)

# Delete chapters and pages if necessary
chapters.delete_chapters(setup.base_url, existing_chapters, matched_chapter_ids, matched_page_ids)
pages.delete_pages(setup.base_url, existing_chapters, matched_page_ids)

logging.info("Done synchronising. All up to date!")