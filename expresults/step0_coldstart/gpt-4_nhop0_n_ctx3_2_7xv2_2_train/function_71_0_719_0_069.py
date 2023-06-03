
import re

def is_spam(message):
    # Spam words and phrases to detect
    spam_keywords = [
        "성공지름길", "정확한 타점", "비밀번호", "광고", "무료거부", "입금", "즉시 할인",
        "수익률", "검증된", "종목상담/추천"
    ]
    
    # Regex patterns for detecting spammy URLs and phone numbers
    url_pattern = r'https?://\S+'
    phone_pattern = r'\d{2,4}[-\s]\d{3,4}[-\s]\d{4}'
    
    # Check for spam keywords in the message
    for keyword in spam_keywords:
        if keyword.lower() in message.lower():
            return True
            
    # Check for spammy URLs and phone numbers in the message
    if re.search(url_pattern, message) or re.search(phone_pattern, message):
        return True
    
    # If none of the checks above match, return False (not spam)
    return False
