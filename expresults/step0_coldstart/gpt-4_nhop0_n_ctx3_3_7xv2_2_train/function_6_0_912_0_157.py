
import re

def is_spam(message):
    spam_indicators = [
        r'(https?://\S+)',  # contains a URL
        r'[0-9]+%',   # contains a percentage
        r'(\b\S+[\d]+\S+\b)',  # contains alphanumeric words
        r'([\d]+[\W\D/\d]{3,}[\D]*)'  # alphanumeric characters with multiple special characters
    ]

    for indicator in spam_indicators:
        if re.search(indicator, message, re.IGNORECASE):
            return True

    return False
