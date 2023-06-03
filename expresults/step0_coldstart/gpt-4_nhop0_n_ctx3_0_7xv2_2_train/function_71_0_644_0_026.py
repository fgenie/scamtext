
import re

def is_spam(message):
    spam_keywords = ['적중', '체험반', '분석', '수익률', '종목', '오픈', '타점']
    spam_url_pattern = re.compile(r'https?://me2\.kr/[^\s]+')

    message = message.lower()
    url_match = spam_url_pattern.search(message)

    if url_match:
        return True

    for keyword in spam_keywords:
        if keyword in message:
            return True

    return False
