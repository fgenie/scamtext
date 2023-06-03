
import re

def is_spam(message):
    # If message contains too many symbols, it might be a spam
    symbols = set("~=₩@\#$%^&*")
    symbol_count = sum(1 for c in message if c in symbols)
    if symbol_count > 5:
        return True
    
    # Check for any suspicious phrases and keywords in the message
    phrases = ['무료수신거부', '이거 사주세요', '종목추천', '신규정보입니다', '좋은 정보 받아가세요', '목표달성기념']
    if any(phrase in message for phrase in phrases):
        return True
    
    # Check for URLs containing suspicious domains
    urls = re.findall(r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\\(\\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', message)
    suspicious_domains = ['me2.kr', 'opcn-kakao.com']
    for url in urls:
        if any(d in url for d in suspicious_domains):
            return True

    # Check for excessive use of numbers and/or letters in the message
    numbers = sum(1 for c in message if c.isdigit())
    letters = sum(1 for c in message if c.isalpha())
    if (numbers > 13 and letters < 10) or (letters > 50 and numbers < 1):
        return True

    # If no suspicious content found, consider the message normal
    return False
