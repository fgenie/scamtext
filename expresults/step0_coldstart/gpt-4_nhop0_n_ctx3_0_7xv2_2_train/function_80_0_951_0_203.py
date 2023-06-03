
import re

def is_spam(message: str) -> bool:
    # Check for multiple lines in a message
    if len(message.splitlines()) > 1:
        return True

    # Check for URL pattern in the message
    url_pattern = re.compile(r'https?://(?:[\w./-])+')
    urls = url_pattern.findall(message)
    if urls:
        return True

    # Check for potential spam keywords (e.g., prize, money, winning, etc.) in the message
    spam_keywords = ['등', '매년', '추천', '입증', '판단', '상담']
    if any(keyword in message for keyword in spam_keywords):
        return True

    return False
