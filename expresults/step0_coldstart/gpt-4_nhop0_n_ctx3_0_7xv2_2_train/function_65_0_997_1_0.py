
import re

def is_spam(text):
    # Check for unusual symbols
    unusual_symbols = re.findall(r'[\u0080-\uFFFF]', text)
    if len(unusual_symbols) > 0:
        return True

    # Check for URL patterns
    url_patterns = [
        r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\\(\\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+',
        r'(?:www\.)?[-a-zA-Z0-9@:%._\\+~#=]{1,256}\.[a-zA-Z0-9()]{1,6}\b([-a-zA-Z0-9()@:%_\\+.~#?&//=-]*)',
        r'(?:kakaosa?\.co\.kr)'
    ]
    if any(re.search(pattern, text) for pattern in url_patterns):
        return True

    # Check for money symbols and values
    money_symbols = re.findall(r'(?<![a-zA-Z0-9])\d{1,3},\d{3}원|(?<![a-zA-Z0-9])[0-9]+만', text)
    if len(money_symbols) > 0:
        return True

    # If none of the above conditions are met, the message is considered normal
    return False
