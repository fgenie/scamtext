
import re

def is_spam(message):
    spam_keywords = ['입', '출', '%', '신', '시', '회', '공', '개', '증', '상', '투', '습', '참', '영', '주']
    normal_keywords = ['진료', '안내', '점심', '문의', '성함', '감사']

    message = message.lower()

    # Check if message contains URLs
    url_pattern = re.compile('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\), ]|(?:%[0-9a-fA-F][0-9a-fA-F]))+')
    urls = re.findall(url_pattern, message)
    if len(urls) > 0:
        return True

    # Check if message contains spam keywords
    for keyword in spam_keywords:
        if keyword in message:
            return True

    # Check if message contains normal keywords
    for keyword in normal_keywords:
        if keyword in message:
            return False

    return False
