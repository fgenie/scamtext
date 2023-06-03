
import re

def is_spam(message):
    spam_keywords = ['광고', '계약', '무료거부', '카톡방', '장 시작전', 'openkakao.io', 'me2.kr']
    url_pattern = re.compile(r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\\(\\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+')

    for keyword in spam_keywords:
        if keyword in message:
            return True
    
    if url_pattern.search(message):
        return True

    return False
