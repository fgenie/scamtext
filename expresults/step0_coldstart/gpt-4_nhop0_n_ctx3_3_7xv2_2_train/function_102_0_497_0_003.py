
import re

def is_spam(message):
    spam_keywords = ['마감임박', '추천주', '현황', '정회원', '차별화', '전략']
    suspicious_url_keywords = ['me2.kr']

    # Check for the presence of spam keywords in the message
    if any(keyword in message for keyword in spam_keywords):
        return True

    # Check for suspicious URLs in the message
    urls = re.findall('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\\(\\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', message)
    if any(any(keyword in url for keyword in suspicious_url_keywords) for url in urls):
        return True

    return False
