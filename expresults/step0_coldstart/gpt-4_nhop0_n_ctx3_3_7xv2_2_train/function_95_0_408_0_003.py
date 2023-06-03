
import re

def is_spam(message):
    spam_keywords = [
        "투자", "상승", "추천", "수익", "종목", "실력", "투자반", "VIP", "계열사합병", "발표예정", "MOU", "적중", "공개"
    ]

    url_pattern = r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\\(\\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+'

    if re.search(url_pattern, message):  # if the message contains a URL
        if any(keyword in message for keyword in spam_keywords):
            return True

    return False
