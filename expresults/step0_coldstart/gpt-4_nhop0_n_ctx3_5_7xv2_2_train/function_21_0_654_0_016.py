
import re

def is_spam(message):
    spam_keywords = ['신청', '입장', '클릭', '종료안내', '제한참여', '기존정보', '목표달성기념', '추천']

    if any(keyword in message for keyword in spam_keywords):
        return True

    url_regex = r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+'
    urls = re.findall(url_regex, message)

    if urls:
        spam_url_keywords = ['openkakao', '신규통합방', 'me2.kr']
        for url in urls:
            if any(keyword in url for keyword in spam_url_keywords):
                return True

    return False
