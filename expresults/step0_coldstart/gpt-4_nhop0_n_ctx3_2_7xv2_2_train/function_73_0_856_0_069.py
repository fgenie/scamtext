
import re

def is_spam(message: str) -> bool:
    # Check for suspicious keywords
    spam_keywords = ['신뢰', '정확한 종목', '균', '코드', '제한참여', '기존정보', '혜택유지', '선 물 거 래']
    for keyword in spam_keywords:
        if keyword in message:
            return True
    
    # Check for suspicious URL patterns
    url_patterns = [r'(http|https)://[^\s]+', r'\b\w+\.\w{2,4}/\w+']
    for pattern in url_patterns:
        urls = re.findall(pattern, message)
        if urls:
            return True
            
    # Check for suspicious number amounts
    suspicious_amounts = [r'\d{1,3}[,\.]\d{3}', r'\d{7}']
    for amount in suspicious_amounts:
        if re.search(amount, message):
            return True

    return False
