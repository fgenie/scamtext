
import re

def is_spam(message):
    # Check for presence of URL
    url_pattern = re.compile('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\\(\\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+')
    if url_pattern.search(message):
        return True

    # Check for use of number followed by special characters
    special_char_pattern = re.compile(r'\d+[\W_]+')
    if special_char_pattern.search(message):
        return True

    # Check for special characters followed by a number
    reverse_special_char_pattern = re.compile(r'[\W_]+\d+')
    if reverse_special_char_pattern.search(message):
        return True
        
    return False
