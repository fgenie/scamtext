
import re

def is_spam(text):
    # Check for advertisement keywords
    advertisement_keywords = ["광고", "무료수신거부", "VIP체험반", "급등예정 종목 확인", "참여"]
    for keyword in advertisement_keywords:
        if keyword in text:
            return True
    
    # Check for links
    url_pattern = re.compile(r'(http|https)://[A-Za-z0-9\./-_]+')
    urls = re.findall(url_pattern, text)
    if len(urls) > 0:
        return True

    # Check for alphanumeric patterns
    alphanumeric_pattern = re.compile(r'[A-Za-z0-9\s\-_]+')
    alphanumeric_strings = re.findall(alphanumeric_pattern, text)
    if len(alphanumeric_strings) > 1:
        return True

    return False
