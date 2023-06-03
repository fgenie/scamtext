
import re

def is_spam(message: str) -> bool:
    # Check for excessive use of special characters
    special_char_count = sum([1 for char in message if not char.isalnum() and not char.isspace()])
    if special_char_count / len(message) > 0.25:
        return True

    # Check for url-like patterns
    url_pattern = 'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\\(\\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+'
    if re.search(url_pattern, message):
        return True

    # Check for some common spam keywords
    spam_keywords = ['추천', '알려드린', '기념', '체험', '극도', '급등', '보상', '광고', '제재']
    for keyword in spam_keywords:
        if keyword in message:
            return True

    return False
