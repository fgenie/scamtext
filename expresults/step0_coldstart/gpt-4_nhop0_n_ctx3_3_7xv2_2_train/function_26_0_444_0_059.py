import re

def is_spam(message):
    
    # Checking for keywords indicating spam messages
    spam_patterns = [
        r'\b(비밀번호|무료수신거부|무료강의|무료거부|성공지름길)\b',
        r'\b\w{2,}\.\w{3,}\b',
        r'%.{0,3}\d{0,4}',
        r'\* [가-힣]+',
        r'^\([^광](.)]',
    ]
    
    for pattern in spam_patterns:
        if re.search(pattern, message):
            return True
    return False