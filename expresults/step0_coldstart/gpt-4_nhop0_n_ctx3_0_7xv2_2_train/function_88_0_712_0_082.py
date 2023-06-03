
import re

def is_spam(message):
    patterns = [
        r'http[s]?://\S+',
        r'%\d+\^',
        r'\d{1,2}:\d{2}',  # Time format hh:mm
        r'\d{1,2}/\d{2}',  # Date format MM/DD
        r'[\d,]+\s*[원]',   # Currency format
        r'상한가',
        r'증권',
        r'[시분초]가',
        r'[%+]\d+',
    ]

    # Flags to track potential spam features
    has_url = False
    has_spam_keywords = False
    has_spam_patterns = False

    # Check for the presence of a URL
    if re.search(patterns[0], message):
        has_url = True

    # Check for spam keywords and patterns in the message
    for pattern in patterns[1:]:
        if re.search(pattern, message):
            has_spam_patterns = True
            break

    # Determine if the message has spam-like features
    if has_url or has_spam_patterns:
        has_spam_keywords = True

    return has_spam_keywords
