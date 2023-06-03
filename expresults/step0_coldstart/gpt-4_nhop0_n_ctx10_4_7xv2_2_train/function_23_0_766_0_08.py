
import re

def is_spam(message):
    # Check for URL patterns
    urls = re.findall(r"(https?://\S+)", message)
    if len(urls) > 0:
        spam_url_keywords = ['kakao', 'opcn', 'me2']
        for url in urls:
            if any(keyword in url for keyword in spam_url_keywords):
                return True

    # Check for suspicious keywords
    spam_keywords = [
        '정회원방', 'Vip', '무료체험반', '광고', '체험반', '종목', '익 절 가', '수익률', 
        '정보방', '목표가', '누적수익률', '무료 주식대학', '손절시', '적중', '한도초과'
    ]
    for keyword in spam_keywords:
        if keyword in message:
            return True

    # Check for excessive special characters
    special_char_count = sum(1 for char in message if not char.isalnum() and not char.isspace())
    if special_char_count > 10:
        return True

    return False

