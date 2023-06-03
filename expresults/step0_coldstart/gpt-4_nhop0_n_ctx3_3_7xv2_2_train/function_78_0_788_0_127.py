
import re

def is_spam(message):
    # Pattern for detecting excessive use of special characters or numbers
    # In spam/nonsensical messages, urls, dates, or alphanumeric codes.
    pattern = r'[\W\d]{3,}'

    # Check for the number of matches
    matches = re.findall(pattern, message)

    # If the number of matches is greater than or equal to 2, it's likely to be spam
    if len(matches) >= 2:
        return True
    else:
        return False
