
import re

def is_spam(message):
    spam_keywords = ['신 청', '새로운 정보방', '초I고', '입장 안내', 'LIVE CA', '비교 한번', '적립금']

    message = message.replace('\n', ' ')

    for keyword in spam_keywords:
        if keyword in message:
            return True

    urls = re.findall(r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\\(\\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', message)
    if urls:
        for url in urls:
            if 'me2.kr' in url or 'openkakao.io' in url:
                return True

    return False
