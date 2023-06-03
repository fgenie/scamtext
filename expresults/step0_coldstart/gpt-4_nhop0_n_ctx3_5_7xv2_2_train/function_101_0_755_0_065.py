
import re

def is_spam(message: str) -> bool:
    # Check for suspicious patterns in the text
    patterns = [
        r'\b(?:[0-9]+,?)+[0-9]+\b', # numbers like 30,000 or 30000
        r'(?:https?://\S{5,})', # urls
        r'\b(?:[a-zA-Z0-9]{5,})\b', # random string more than 5 characters
    ]
    spam_indicator_count = 0
    for pattern in patterns:
        if re.search(pattern, message):
            spam_indicator_count += 1

    # If more than one pattern is found, the message is probably spam
    return True if spam_indicator_count > 1 else False
