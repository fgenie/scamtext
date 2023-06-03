
import re

def is_spam(message):
    spam_keywords = ['원계약', '광고', '지원금', '지급', '배당', '투자', '상한가', '수익', '안전거래소', '월 최대']
    url_pattern = re.compile(r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+')
    openkakao_pattern = re.compile(r'openkakao\.at/\w+')
    me2_pattern = re.compile(r'me2\.kr/\w+')

    if url_pattern.search(message) or openkakao_pattern.search(message) or me2_pattern.search(message):
        return True

    for keyword in spam_keywords:
        if keyword in message:
            return True
            
    return False
