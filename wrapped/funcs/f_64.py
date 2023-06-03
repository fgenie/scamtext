
import re

def is_spam(message):
    message = message.lower()

    # Check for common spam keywords
    spam_keywords = ['정회원', '추천주', '클릭', '참여', '체험반', '광고', '새 가족', '※', '적립금', '방문', '무료수신거부', '적중']
    for keyword in spam_keywords:
        if keyword in message:
            return True

    # Check for patterns specific to spam messages
    url_pattern = re.compile(r'(http|https)://[a-zA-Z0-9./]+')
    percentage_pattern = re.compile(r'\d+%')
    code_pattern = re.compile(r'\w+\d+|코드:\w+')
    key_pattern = re.compile(r'key\s*:?\s*\d+', re.IGNORECASE)
    
    if (url_pattern.search(message) and percentage_pattern.search(message)) or \
       (code_pattern.search(message) or key_pattern.search(message)):
        return True

    return False
