
import re

def is_spam(message):
    # Check for common spam patterns.
    url_pattern = re.compile(r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+')
    spam_keywords = ["광고", "비트", "단타거래", "무료거부", "월 천 고정수입", "파이널VIP체험반", "4월파이널VIP체험반", "종목드리며 시작"]
    
    if re.search(url_pattern, message) or any(keyword in message for keyword in spam_keywords):
        return True
    else:
        return False
