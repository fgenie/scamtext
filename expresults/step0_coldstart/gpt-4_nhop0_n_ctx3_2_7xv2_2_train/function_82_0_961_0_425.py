def is_spam(message):
    import re

    # Check for url in the message
    url_pattern = re.compile(r'https?://(?:[-\w.]|(?:%[\da-fA-F]{2}))+')
    urls = re.findall(url_pattern, message)

    # Check for unusual/unwanted characters
    unusual_chars = ['!', '↑', '*', '\\', '^', '~', '▼', '▲']
    has_unusual_chars = any(char in message for char in unusual_chars)

    # Check for non-alphabetic sequences
    non_alpha_pattern = re.compile(r'\W+')
    non_alpha_seq = re.findall(non_alpha_pattern, message)

    if len(urls) > 0 or has_unusual_chars or len(non_alpha_seq) > 3:
        return True
    else:
        return False