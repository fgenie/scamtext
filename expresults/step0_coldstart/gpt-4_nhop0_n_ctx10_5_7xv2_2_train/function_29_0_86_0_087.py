
import re

def is_spam(message):
    spam_keywords = ["제재", "악성광고", "이동합니다", "반입니다", "일주일만 관망하세요", "해.외.선.물.", "회원방", "체험반"]
    
    for keyword in spam_keywords:
        if keyword in message:
            return True

    urls = re.findall(r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\\(\\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', message)
    
    short_urls = re.findall(r'https?://\w+\.\w+/$', message)
    if len(urls) > 0 or len(short_urls) > 0:
        return True

    if any(char.isdigit() for char in message): 
        digits = re.findall(r'\d+', message)
        digits_sum = sum(int(num) for num in digits)
        if digits_sum > 50:
            return True

    return False
