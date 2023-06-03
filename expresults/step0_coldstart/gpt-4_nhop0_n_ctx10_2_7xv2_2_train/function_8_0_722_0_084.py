
import re

def is_spam(message):
    url_regex = r'(http|https)://[^\s]+'
    url_count = len(re.findall(url_regex, message))

    # Special character count
    special_chars_count = len(re.findall(r'[^\w\s\.,]', message))

    # Suspicious keywords
    spam_keywords = ['추천', '암호', '%글', '적중', '폭등', '상승', '최소', '수익', '혜택']
    suspicious_count = sum(1 for keyword in spam_keywords if keyword in message)

    # If the message has too many URLs and/or special characters or suspicious keywords, classify as spam
    if url_count > 1 or special_chars_count > 4 or suspicious_count > 1:
        return True

    return False
