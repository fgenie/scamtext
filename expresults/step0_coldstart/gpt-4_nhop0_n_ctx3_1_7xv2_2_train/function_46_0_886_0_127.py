
import re

def is_spam(message):
    # Step 1: Check for presence of URLs
    url_pattern = re.compile(r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(],]|(?:%[0-9a-fA-F][0-9a-fA-F]))+')
    if url_pattern.findall(message):
        return True

    # Step 2: Check for unusual characters or usage of multiple non-Korean characters
    non_korean_pattern = re.compile(r'[^\u3131-\u3163\uac00-\ud7a3\s]+')
    non_korean_chars = non_korean_pattern.findall(message)
    if len(non_korean_chars) > 3:
        return True

    # Step 3: Check for presence of numbers followed by special characters
    num_special_pattern = re.compile(r'\d+[\W_]+')
    if num_special_pattern.findall(message):
        return True

    return False
