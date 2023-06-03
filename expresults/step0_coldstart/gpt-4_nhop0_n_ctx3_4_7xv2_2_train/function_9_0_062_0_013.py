
import re

def is_spam(text):
    # Define some common spam message characteristics
    spam_keywords = ["비밀 종목", "투자의 귀재", "광고", "지금 저점", "에코프로", "미국 나스닥 지수", "새로운 테마", "상승 추세"]
    url_pattern = re.compile(r"http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+")

    # Check if the message contains spam keywords
    has_spam_keywords = any(keyword in text for keyword in spam_keywords)

    # Check for urls
    has_urls = bool(url_pattern.search(text))

    # If the message contains both spam keywords and urls, classify as spam
    if has_spam_keywords and has_urls:
        return True
    else:
        return False
