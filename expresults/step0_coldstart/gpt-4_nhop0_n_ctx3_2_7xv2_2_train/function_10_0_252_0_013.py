
import re

def is_spam(text):
    url_pattern = re.compile(r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\\(\\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+')
    spam_words = ['비밀 종목', '매집 예정', '무료거부', '광고', '약속', '신규인원', '마감', '공시발표', '보상', '클릭', '수익']
    normal_words = ['저녁', '밥', '돈', '묵자']

    if url_pattern.search(text):
        if any(spam_word in text for spam_word in spam_words):
            return True

    if all(normal_word not in text for normal_word in normal_words):
        return False
    else:
        return False
