
import re

def is_spam(message):
    message = message.strip()

    # Check for consecutive use of special characters
    special_chars = re.search(r"[\!@#$%^&*()_+\[\]{}\\|;':\",./<>?]{2,}", message)
    if special_chars:
        return True

    # Check for URLs
    urls = re.findall(r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\\(\\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', message)
    if len(urls) > 1 or (len(urls) == 1 and len(message.split()) <= 4):
        return True

    # Check for a high ratio of special characters to letter characters
    special_char_count = sum(c.isalnum() == False for c in message)
    letter_count = sum(c.isalnum() for c in message)
    if special_char_count / max(letter_count, 1) > 0.4:
        return True

    # Check for a high ratio of numbers to letter characters
    digit_count = sum(c.isdigit() for c in message)
    if digit_count / max(letter_count, 1) > 0.6:
        return True

    return False
