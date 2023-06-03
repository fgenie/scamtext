
import re

def is_spam(message):
    spam_indicators = [
        r'\d+[.,]\d+%',
        r'https?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*]+)+',
        r'[.,-](?:\s?COM|\d)',
        r'\d{6,}',
        r'\W[a-zA-Z0-9]+\W?\d\W+',
    ]

    for indicator in spam_indicators:
        if re.search(indicator, message):
            return True

    return False
