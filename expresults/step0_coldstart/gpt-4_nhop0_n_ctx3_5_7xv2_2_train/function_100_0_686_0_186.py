
import re

def is_spam(message):
    # Define common spam keywords and patterns
    spam_keywords = ["추천주", "종목", "코드", "일평균", "출거", "세요"]

    # Check for excessive usage of special characters
    special_chars = re.findall('[^가-힣0-9a-zA-Z\s]', message)
    special_char_ratio = len(special_chars) / len(message)

    # Check for URL patterns
    urls = re.findall('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', message)

    keyword_count = 0
    for keyword in spam_keywords:
        if keyword in message:
            keyword_count += 1

    if keyword_count >= 2 or special_char_ratio >= 0.2 or len(urls) > 0:
        return True
    else:
        return False
