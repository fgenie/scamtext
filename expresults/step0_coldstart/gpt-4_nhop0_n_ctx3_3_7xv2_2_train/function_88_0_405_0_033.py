
import re

def is_spam(message):
    # Check for suspicious keywords
    spam_keywords = ['긴급입수', '정식허가', '상한가', '회사공시', '수익률', '종목', '목표가', '익 절 가', '누적수익률', '부업']
    
    for keyword in spam_keywords:
        if keyword in message:
            return True
    
    # Check for multiple URLs
    url_pattern = r'https?://\S+'
    urls = re.findall(url_pattern, message)
    if len(urls) > 1:
        return True

    return False
