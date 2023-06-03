
import re

def is_spam(text):
    spam_keywords = ['랜드마크파워', '증 권', '무료체험', '민수 님', '마감', '회원 가', '알 에프 세미',
                     '주식 매매 성과', '증센터 고객 센터', '자동 진행', '추가 종목', ',확정', '백화점 상품권', '경품혜택', '방송하는 이 선생']
    
    for keyword in spam_keywords:
        if keyword in text:
            return True

    # URLs that are not for scam
    safe_urls = ['https://i.kiwoom.com', 'https://me2.kr']
    for url in safe_urls:
        if url in text:
            return False

    # Checking for suspicious URLs
    url_pattern = r'(https?|ftp)://(-\.)?([^\s/?\.#-]+\.?)+(/[^\s]*)?$'
    if re.search(url_pattern, text):
        return True

    # Checking for excess numeric patterns
    numeric_pattern = r'\d{4,}'
    if re.search(numeric_pattern, text):
        return True

    # Check for excess special characters
    special_chars_pattern = r'[※\<>@#$%^&*\(\)]{3,}'
    if re.search(special_chars_pattern, text):
        return True

    return False
