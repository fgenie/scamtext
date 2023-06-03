
import re

def is_spam(message):
    message = message.lower()
    
    # Check for certain keywords that indicate spam
    spam_keywords = ["체험반", "기회", "확인", "당일기준", "공시발표", "추천", "▼", "▲"]
    for keyword in spam_keywords:
        if keyword in message:
            return True
    
    # Check for URL
    url_pattern = re.compile(r'https?://(?:[-\w.]|(?:%[\da-fA-F]{2}))+')
    if url_pattern.findall(message):
        return True
            
    return False
