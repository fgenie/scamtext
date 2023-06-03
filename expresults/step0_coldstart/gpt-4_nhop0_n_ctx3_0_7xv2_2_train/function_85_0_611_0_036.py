
import re

def is_spam(message: str) -> bool:
    # Regular expression patterns to detect spam
    spam_patterns = [
        r'\d+원\s*으로\s*\d+원',
        r'\d+\s*준비',
        r'\d+日',
        r'https?://[a-zA-Z0-9._%+-/]{2,20}'
    ]

    # Check if any spam pattern is present in the message
    for pattern in spam_patterns:
        if re.search(pattern, message):
            return True

    # If no spam pattern is found, return False
    return False
