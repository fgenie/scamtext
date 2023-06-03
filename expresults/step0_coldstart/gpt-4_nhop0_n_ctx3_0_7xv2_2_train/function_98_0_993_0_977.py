
import re

def is_spam(message):
    spam_patterns = [
        r'https?:\/\/\S+',  # URLs
        r'openkakao\.io\/\S+',  # OpenKakao URLs
        r'\d+%↑',  # Percentage increase followed by an up arrow
        r'[가-힣]:?',  # Hangul characters followed by a colon 
    ]

    for pattern in spam_patterns:
        if re.search(pattern, message):
            return True

    return False
