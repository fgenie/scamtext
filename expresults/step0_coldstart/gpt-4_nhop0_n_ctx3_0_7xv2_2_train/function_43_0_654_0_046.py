
import re

def is_spam(message):
    spam_keywords = ['축하합니다', '당첨', '추천주', '시황', '분석', '수익률 100%', '부업실현', '월 천 고정수입']
    has_numeric = bool(re.search(r'\d', message))
    has_url = bool(re.search(r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\\(\\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', message))

    if any(keyword in message for keyword in spam_keywords) or (has_numeric and has_url):
        return True

    return False
