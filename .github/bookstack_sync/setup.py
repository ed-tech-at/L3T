import bookstack
import os
import argparse
import logging
from datetime import datetime
from pathlib import Path
import sys
from glob import glob

# Local files
import utilities

# Global Variables
api = None
headers = None
base_url = None


# Initialization - Setup Bookstack API
def init():
	# Setup logging incl. different levels as argument
	args = parse_args()
	log_level = getattr(logging, args.log_level)
	logging.basicConfig(level=log_level, format="%(levelname)s [%(asctime)s]: %(message)s")

	# Setup Bookstack API
	global api, headers, base_url
	api, headers, base_url = setup_api()


# Check for methods in API
def has_generated_methods(api):
	return any(
		callable(getattr(api, attr)) and attr.startswith(('get_', 'post_', 'put_', 'delete_'))
		for attr in dir(api)
	)


# Setup for the API sever
def setup_api():
	base_url = os.getenv("BOOKSTACK_URL")
	token_id = os.getenv("BOOKSTACK_TOKEN_ID")
	token_secret = os.getenv("BOOKSTACK_TOKEN_SECRET")

	headers = {"Authorization": f"Token {token_id}:{token_secret}"}
	api = bookstack.BookStack(base_url, token_id=token_id, token_secret=token_secret)
	utilities.retry_request(api.generate_api_methods, context="trying to initiate a connection to the server")

	if not has_generated_methods(api):
		logging.critical("API method generation failed. Aborting sync.")
		sys.exit(1)
	
	return api, headers, base_url


# Setup for passing logging level argument
def parse_args():
	parser = argparse.ArgumentParser(description="Sync BookStack-Contents for the Book L3T.")
	parser.add_argument(
		"-l", "--log-level",
		default="INFO",
		choices=["DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL"],
		type=str.upper,
		help="Depth of logging information (default: INFO)"
	)
	return parser.parse_args()


# Check for book folder (e.g. "00_L3T") within repository 
def book_base_path():
    candidates = [
        directory for directory in os.listdir(".")
        if os.path.isdir(directory) and directory.startswith("00_")
    ]

    for candidate in candidates:
        # Check if 00_*.md file exists inside candidate
        md_files = glob(os.path.join(candidate, "00_*.md"))
        img_folder = os.path.join(candidate, "img")
        if len(md_files) == 1 and os.path.isdir(img_folder):
            return candidate, md_files[0]

    logging.critical("No valid book folder with a single 00_*.md-file and an img-folder found. Aborting sync.")
    sys.exit(1)
