
import re

def is_spam(message):
    spam_keywords = ['종목추천', '무료', '수익', '방문해주세요', '후회안합니다', '단타정보', '트레이딩']
    spam_url_pattern = re.compile(r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\\(\\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+')

    message = message.lower()
    if any(keyword in message for keyword in spam_keywords) or spam_url_pattern.search(message):
        return True
    else:
        return False
