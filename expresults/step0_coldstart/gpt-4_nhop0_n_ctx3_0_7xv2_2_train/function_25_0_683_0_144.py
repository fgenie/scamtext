
import re

def is_spam(message):
    # Check for typical spam-related keywords
    spam_keywords = ['광고', '지원금', '선물', '혜택', '해외', '비밀번호', '복권', '가입', '특별', '상품권', '환전']
    
    for keyword in spam_keywords:
        if keyword in message:
            return True

    # Check for unusual URL patterns
    url_pattern = re.compile(r'https?://\S+')
    urls = url_pattern.findall(message)
    
    for url in urls:
        if any(x in url for x in ['.kr', 't.ly']):
            return True

    # Check for an unusually high percentage of special characters
    special_chars_ratio = len(re.findall(r'[^\w\s]', message)) / len(message)
    if special_chars_ratio > 0.15:
        return True

    return False
