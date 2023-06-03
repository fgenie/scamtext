
import re

def is_spam(message):
    # Check for url presence
    url_pattern = re.compile(r'https?://\S+')
    if url_pattern.search(message):
        return True

    # Check for special characters like percentage, up-arrow, etc.
    spam_chars = ['%', '↑', '▼', '▲']
    for char in spam_chars:
        if char in message:
            return True

    # Check if the message if consecutive capital letters or number patterns
    cap_pattern = re.compile(r'[가-힣]*[A-Z가-힣0-9\s]+'+'\(?'+'\w+'+'\)?')
    if cap_pattern.match(message):
        return True

    return False
