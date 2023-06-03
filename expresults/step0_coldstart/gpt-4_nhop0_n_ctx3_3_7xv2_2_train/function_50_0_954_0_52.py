
import re

def is_spam(message):
    # Check if the message contains typical spam keywords
    spam_keywords = ["광고", "적중", "무료거부", "일주일", "VTI", "차별화 된", "실력으로 입증", "실력보셨죠?"]

    for keyword in spam_keywords:
        if keyword in message:
            return True

    # Check if message contains a URL with a short link (me2.kr, bit.ly, etc.)
    short_link_patterns = [r"https?://me2\.kr/\S+", r"\b(?:http|https)://(?:bit\.ly|goo\.gl|is\.gd|tinyurl\.com)\S+", r"https?://dokdo\.in/\S+"]

    for pattern in short_link_patterns:
        if re.search(pattern, message):
            return True
            

    # Check if the message contains unusual capitalization or special characters
    unusual_caps = sum([1 for char in message if char.isupper()]) / len(message) > 0.5
    special_chars = re.search(r"[\[!#$%&\'\"()*+,./:;<=>?@\^_`{|}~-]", message)

    if unusual_caps or special_chars:
        return True

    return False
