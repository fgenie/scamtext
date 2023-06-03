
import re

def is_spam(text):
    # Check for common spam keywords and phrases
    keywords = ["상한가확정", "추천주", "배송 제한", "참여", "돌파", "실력입증", "체험반", "투자반", "※"]
    for keyword in keywords:
        if keyword in text:
            return True

    # Check for presence of a URL pattern
    url_pattern = re.compile(r'https?://[^\s<>"]+|www\.[^\s<>"]+')
    if url_pattern.search(text):
        return True

    # If none of these conditions are met, classify the text as not spam
    return False
