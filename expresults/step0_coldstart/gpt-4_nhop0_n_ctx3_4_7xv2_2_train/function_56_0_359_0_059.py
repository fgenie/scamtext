
import re

def is_spam(message):
    # Checking for excessive special characters, capital letters, or numbers
    special_chars = re.findall(r'[\W]', message)
    capital_chars = re.findall(r'[A-Z]', message)
    digits = re.findall(r'\d', message)
    
    if len(special_chars) > len(message) * 0.5 or len(capital_chars) > len(message) * 0.4 or len(digits) > len(message) * 0.2:
        return True
    
    # Checking for common spam phrases
    spam_phrases = ["(광고)", "특별찬스", "적립금", "C.A.S.H", "무료수신거부", "월요일부터 시작하는 VIP체험반", "여의도사람들", "인증번호", "할인", "프로모션", "클릭", "확인해주세요", "EVENT", "SALE"]
    
    for phrase in spam_phrases:
        if phrase in message:
            return True

    # Checking for excessive URLS
    urls = re.findall(r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', message)
    
    if len(urls) > 1:
        return True
    
    return False
