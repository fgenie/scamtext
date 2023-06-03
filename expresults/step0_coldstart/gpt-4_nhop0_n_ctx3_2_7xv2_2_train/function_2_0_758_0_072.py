
import re

def is_spam(message):
    # Check for presence of URLs
    url_pattern = r'(https?://\S+)|(\w+\.\w+\.\w+\S*)'
    if re.search(url_pattern, message):
        return True

    # Check for presence of specific spam-related keywords
    spam_keywords = ['광고', 'VIP투자', '종.목', '수익', '목표가', '안녕하세요 기대하셔도 좋습니다',
                     '무료거부', '전세', '대림이편한세상헤이리', '폭등예상']
    for keyword in spam_keywords:
        if keyword in message:
            return True

    # Check for presence of multiple special characters
    special_characters = ['▲', '★', '▼', '▶', '■']
    count = 0
    for char in message:
        if char in special_characters:
            count += 1
            if count >= 3:
                return True

    return False
