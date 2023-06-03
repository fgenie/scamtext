
import re

def contains_url(text):
    url_pattern = re.compile(r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\\(\\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', re.IGNORECASE)
    return bool(url_pattern.search(text))

def is_korean(text):
    hangul = re.compile('[\u3131-\u3163\uac00-\ud7a3]+')
    return bool(hangul.search(text))

def is_spam(text):
    if contains_url(text) and is_korean(text):
        return True
    if len(text.split()) <= 3:
        return False
    spam_keywords = ["증권", "종목", "매수", "상승", "익절", "선입수", "오픈", "공시", "이번주"]
    for keyword in spam_keywords:
        if keyword in text:
            return True
    return False
