
import re

def is_spam(message):
    keywords = [
        "축하합니다",
        "알려드린",
        "만원으로",
        "30,000",
        "AI",
        "MOU",
        "돌파",
        "적중",
        "чыч-чыч"
    ]
    
    # These URL patterns tend to exist in spam messages than in normal ones
    spam_url_patterns = [
        r'https?:\/\/ko\.gl\/',
        r'https?:\/\/me\d\.kr\/',
        r'https?:\/\/url\.kr\/',
        r'https?:\/\/bit\.ly\/'
    ]

    # Check if any keyword exists in the message
    for keyword in keywords:
        if keyword in message:
            return True

    # Check if any spam URL pattern exists in the message
    for pattern in spam_url_patterns:
        if re.search(pattern, message):
            return True

    # Return False if no spam keyword or pattern is found
    return False
