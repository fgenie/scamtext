
import re

def is_spam(message):
    # Check for keywords often found in spam messages
    spam_keywords = ['추천', '무료', '충전이벤트', '계열', 'VIP', '다운']
    
    for keyword in spam_keywords:
        if keyword in message:
            return True
    
    # Check for the presence of URLs
    url_pattern = re.compile(r'https?://[\w\.-]+\.[\w\.-]+(/[A-Za-z0-9\.\-_]*)*')
    urls = re.findall(url_pattern, message)
    
    if urls:
        return True
    
    # Check for Korean specific spam characteristics
    brackets_pattern = re.compile(r'\[.+?\]')
    brackets_text = re.findall(brackets_pattern, message)
    if brackets_text:
        return True
    
    # If none of the spam indicators are found, classify as a normal message
    return False
