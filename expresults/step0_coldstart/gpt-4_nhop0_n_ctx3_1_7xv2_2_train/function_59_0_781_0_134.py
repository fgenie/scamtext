
import re

def is_spam(message):
    # Check for common spam patterns
    url_pattern = re.compile(r'https?://\S+')
    phone_pattern = re.compile(r'\d{3,4}[-\s]?\d{3,4}[-\s]?\d{4}')
    excessive_special_chars = re.compile(r'[\W_]{4}')

    # Look for urls, phone numbers, and excessive special characters
    url_match = url_pattern.search(message)
    phone_match = phone_pattern.search(message)
    excessive_special_chars_match = excessive_special_chars.search(message)

    # If any one of the patterns is found, classify the message as spam
    if url_match or phone_match or excessive_special_chars_match:
        return True
    else:
        return False
