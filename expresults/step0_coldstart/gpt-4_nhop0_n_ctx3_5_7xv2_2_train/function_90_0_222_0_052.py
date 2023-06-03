
import re

def is_spam(message):
    # Check for excessive use of special characters
    special_char_count = len(re.findall(r'[!?*<>^-]', message))
    if special_char_count / len(message) >= 0.2:
        return True

    # Check for unusual URL structures and multiple URLs
    url_count = len(re.findall(r'https?://(?:[-\w.]|(?:%[\da-fA-F]{2}))+', message))
    if url_count > 1 or url_count / len(message) >= 0.15:
        return True

    # Check for combination of characters and numbers in message (often seen in spam messages)
    if len(re.findall(r'([a-zA-Z]{1,}[0-9]{1,})|([0-9]{1,}[a-zA-Z]{1,})', message)) > 1:
        return True

    return False
