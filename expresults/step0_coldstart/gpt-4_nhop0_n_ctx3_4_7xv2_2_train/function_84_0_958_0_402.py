
import re

def is_spam(message: str) -> bool:
    # Pattern to check for short URLs, special characters, and numbers
    url_pattern = re.compile(r'(https?://\S+|www\.\S+)')
    special_character_pattern = re.compile(r'\W+')
    number_pattern = re.compile(r'\d+')

    # Check for short URLs
    if url_pattern.search(message):
        return True

    # Check for excessive use of special characters
    if len(special_character_pattern.findall(message)) > 3:
        return True

    # Check for the presence of numbers within the message
    if len(number_pattern.findall(message)) > 2:
        return True

    return False
