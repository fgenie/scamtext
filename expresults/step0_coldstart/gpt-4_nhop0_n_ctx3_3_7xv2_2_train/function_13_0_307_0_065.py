
import re

def is_spam(message):
    spam_keywords = ['무료', '필요하시면', '후회안합니다', '추천', '정보', '확인', '이벤트', '대출', '상품', '사이트']

    # Check for suspicious patterns
    has_suspicious_constants = any(keyword in message for keyword in spam_keywords)
    has_unusual_spaces = bool(re.search(r'\s{2,}', message))
    has_many_capitalized = bool(re.search(r'[A-Z|ㄱ-ㅎ|ㅏ-ㅣ]{4,}', message))
    
    return has_suspicious_constants and (has_unusual_spaces or has_many_capitalized)
