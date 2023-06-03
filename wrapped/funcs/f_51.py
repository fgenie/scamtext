
import re

def is_spam(message: str) -> bool:
    # Patterns to detect spam
    url_pattern = re.compile(r'https?://\S+|www\.\S+')  # URLs
    num_pattern = re.compile(r'\d{4,}')  # Large numbers (4 or more digits)
    special_char_pattern = re.compile(r'[!"#$%&\'()*+,-./[\\\]^_`{|}~]')  # Special characters

    # Filters to identify spam
    has_url = bool(url_pattern.search(message))
    has_long_num = bool(num_pattern.search(message))
    has_special_chars = bool(special_char_pattern.search(message))

    # If the message contains URLs, large numbers or special chars, classify it as spam
    if has_url or has_long_num or has_special_chars:
        return True
    else:
        return False
