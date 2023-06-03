
import re

def is_spam(text: str) -> bool:
    # Check for common spam indicators
    spam_keywords = ['축하', '당첨', '추천주', '시황', '분석', '수익률', 'bit.ly', 'VVIP', '최신 종목 추천', '수익', '비밀번호', '종목', '친추', '포인트', '출금', '이벤트', '텔레그램', '독보적인 메이저', '계열']
    
    # Check for consecutive uppercase characters and special character ! or ?
    consecutive_uppercase = re.compile(r'([A-Z|가-힣|0-9]+[!|?]+)+')

    for keyword in spam_keywords:
        if keyword in text:
            return True
    
    if consecutive_uppercase.findall(text):
        return True
    
    return False
