
import re

def is_spam(message):
    spam_keywords = ['고정수입', '성공했어요', '추천주', '회사공시', '수익률', '종목 확인', '목표가', '익 절 가', '누적수익률', '전문가 경력']
    url_pattern = re.compile(r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\\(\\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+')

    if url_pattern.search(message) and any(keyword in message for keyword in spam_keywords):
        return True
    return False
