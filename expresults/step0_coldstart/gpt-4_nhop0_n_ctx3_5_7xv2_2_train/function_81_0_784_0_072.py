
import re

def is_spam(message: str) -> bool:
    # Check for spam keywords and suspicious URLs
    spam_keywords = ['VIP', '제재', '악성', '광고', '체험', '공시', '정보', '혜택']
    url_pattern = re.compile(r'https?://[^\s]+')

    # Check for spam keywords in the message
    for keyword in spam_keywords:
        if keyword in message:
            return True

    # Check for suspicious URLs in the message
    if url_pattern.search(message):
        return True

    # Message is likely not spam
    return False
