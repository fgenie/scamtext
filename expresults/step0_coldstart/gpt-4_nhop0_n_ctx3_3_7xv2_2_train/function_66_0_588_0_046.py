
import re

def is_spam(message: str) -> bool:
    # Check for URL shorteners, potentially spam-related
    url_shorteners = ['me2.kr', 'ktalk.org', 'kakaos.co']
    for url in url_shorteners:
        if url in message:
            return True

    # Check for common spam words and phrases
    spam_keywords = [
        '축하합니다', '온라인 GAME', 'VIP 담당 에이전시', '고객님 전달',
        '신규 첫충', '텔레그램 친추', '무제한 충전이벤트', '최소20%'
    ]
    for keyword in spam_keywords:
        if keyword in message:
            return True

    # Check for specific patterns, such as phone numbers or email addresses
    phone_pattern = re.compile(r'\d{3}[-\.\s]??\d{3}[-\.\s]??\d{4}')
    email_pattern = re.compile(r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}')
    if phone_pattern.search(message) or email_pattern.search(message):
        return True

    return False
