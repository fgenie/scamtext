
import re

def is_spam(text):
    keywords = ["광고", "무료거부", "▼확인▼", "https://", "vvip체험반", "↑ 돌파!", "일주일", "원"]

    # Checking for the presence of any spam keywords in the text
    for keyword in keywords:
        if keyword in text:
            return True

    # Checking for the presence of percentage and number together in the text
    percentage_re = re.compile(r"\d+%")
    if percentage_re.search(text):
        return True

    # Checking for the presence of unusual special characters occurring together as potential spam indicator
    special_chars_re = re.compile(r"[*]+")
    if special_chars_re.search(text):
        return True

    return False
