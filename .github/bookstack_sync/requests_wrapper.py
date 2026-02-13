import bookstack
import logging
import time


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