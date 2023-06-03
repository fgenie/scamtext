
import re

def is_spam(message):
    message = message.lower()
    
    # Check for common spam messages characteristics
    spam_keywords = ['(광고)', '추천주', '수익', '주식', '종목', '무료거부', '지원금', '매일강의', '해외선물', '매매', '비밀번호']
    for keyword in spam_keywords:
        if keyword in message:
            return True
    
    # Check for URLs using regular expressions
    url_pattern = re.compile(r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\\(\\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+')
    urls = url_pattern.findall(message)
    if urls:
        return True

    # Check for phone numbers using regular expressions
    phone_pattern = re.compile(r'\d{2,4}-\d{2,4}-\d{4}')
    phone_numbers = phone_pattern.findall(message)
    if phone_numbers:
        return True

    return False
