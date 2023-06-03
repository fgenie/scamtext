
import re

def is_spam(msg: str) -> bool:
    # Check for typical spam keywords and spammy URL patterns
    spam_keywords = ['년지원금', '진료비', '경제부기자', '안녕하세요', '지급!', 'ab늪.er', '단독입수하', '보내드리', '_내일', '일 일', '특별 이벤트']
    spammy_url_patterns = [r'(http|https)://[\w./-]+', r'bit\.ly/[!-~]+'] 
    
    # Check for spam keywords
    for keyword in spam_keywords:
        if keyword in msg:
            return True
    
    # Check for spammy URLs
    for pattern in spammy_url_patterns:
        if re.search(pattern, msg):
            return True
            
    return False
