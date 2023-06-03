
import re

def is_spam(message: str) -> bool:
    # Check for presence of URLs
    url_pattern = r'(https?://\S+|http?://\S+|www\.\S+)'
    if re.search(url_pattern, message):
        return True

    # Check for presence of numbers followed by special characters or letters
    number_pattern = r'\d+[\W|\w]'
    if re.search(number_pattern, message):
        return True

    # Check for presence of special characters with characters or numbers
    special_char_pattern = r'[\W|\w]\d+'
    if re.search(special_char_pattern, message):
        return True

    # If none of the patterns are found, consider the message as normal
    return False
