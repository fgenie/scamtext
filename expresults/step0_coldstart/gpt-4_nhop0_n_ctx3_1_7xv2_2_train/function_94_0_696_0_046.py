
import re

def is_spam(message):
    # Convert message to lowercase
    msg = message.lower()
    
    # Check for common spam keywords and urls
    spam_keywords = ['광고', '출시 이벤트', '오픈카톡방', '계. 약.', '적중', '오픈합니다', '무료거부']
    url_pattern = re.compile(r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\\(\\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+')    
    
    if any(keyword in msg for keyword in spam_keywords) or url_pattern.findall(msg):
        return True
    else:
        return False
