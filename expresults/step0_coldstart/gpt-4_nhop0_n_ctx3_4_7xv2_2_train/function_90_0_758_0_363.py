
import re

def is_spam(message: str) -> bool:
    # Check for URL shorteners
    url_shorteners = ['me2.kr', 'bit.ly', 'tinyurl.com', 'goo.gl']
    for shortener in url_shorteners:
        if shortener in message:
            return True

    # Check for spam words
    spam_words = ['체험반', '무료', '상승', '특허', 'VIP', '최소']
    for word in spam_words:
        if word in message:
            return True

    # Check for overuse of special characters
    if re.search(r'[!@#$%^*+=(){}<> ]+', message):
        special_chars = re.findall(r'[!@#$%^*+=(){}<> ]+', message)     
        total_len = len(special_chars)
        if total_len / len(message) >= 0.2:
            return True

    return False
