
import re

def is_spam(message):
    message = message.lower()

    spam_keywords = ['원', '단독선입수', '배터리', '투자', '추천', '혜택', '쿠폰']
    url_regex = r"(https?:\/\/[^\s]+)"
    excessive_chars = ["!", "?", "@", "#", "$", "%", "&", "*", "=", "+", "-"]

    # Check for spam keywords
    for keyword in spam_keywords:
        if keyword in message:
            return True

    # Check for URLs
    urls = re.findall(url_regex, message)
    if len(urls) > 0:
        return True

    # Check for excessive special characters
    special_char_count = sum([message.count(char) for char in excessive_chars])
    if special_char_count > 3:
        return True

    return False
