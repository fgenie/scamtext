
import re

def is_spam(message):
    spam_keywords = ['VIP투자반', '지니틱스', '4주차체험반', '축하합니다', 'vvip체험반', '기회', '카톡방', '정회원방', '소니드', '벳썸']

    url_regex = r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\\(\\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+'
    emoji_regex = r'[\U0001F600-\U0001F64F]|[\U0001F900-\U0001F9FF]|[\U0001F300-\U0001F5FF]|[\U0001F680-\U0001F6FF]|[\U0001F1E0-\U0001F1FF]'

    urls_found = re.findall(url_regex, message)
    emojis_found = re.findall(emoji_regex, message)

    if len(urls_found) > 0 or len(emojis_found) > 0:
        for keyword in spam_keywords:
            if keyword in message:
                return True
    return False
