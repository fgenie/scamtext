
import re

def is_spam(message):
    # Check if the message contains url
    url_pattern = re.compile(r'https?://[^\s]+')
    urls = url_pattern.findall(message)
    if len(urls) > 0:
        return True

    # Check for specific spammy patterns
    spam_patterns = [
        r'\d{1,2}월',
        r'\d{1,2}주차',
        r'\d{1,2}시',
        r'\d{1,2}계',
        r'\d{1,2}약',
        r'VIP',
        r'무료거부',
        r'지원금',
        r'참여',
    ]

    for spam_pattern in spam_patterns:
        if re.search(spam_pattern, message):
            return True

    return False
