
import re

def is_spam(message: str) -> bool:
    # Check for common spam keywords
    spam_keywords = ['광고', '제공', '상담환영', '무료거부', '축하합니다', '클릭', '현황', '종목']
    for keyword in spam_keywords:
        if keyword in message:
            return True
    
    # Check for URLs
    url_pattern = re.compile(r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\\(\\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+')
    urls = re.findall(url_pattern, message)
    if len(urls) > 0:
        return True
    
    # Check for number patterns, such as dates or percentages
    number_pattern = re.compile(r'\d{1,}\.?\d{0,}%?')
    if re.search(number_pattern, message):
        return True
    
    return False
