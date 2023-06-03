
import re

def is_spam(text):
    # Check for spam keywords
    spam_keywords = ['VIP', '무료', '추천', '수익', '체험반', '오파스넷', '공시발표', '단독입수']
    for keyword in spam_keywords:
        if keyword in text:
            return True

    # Check for URL shorteners
    url_shorteners = ['me2.kr']
    for shortener in url_shorteners:
        if shortener in text:
            return True

    # Check for multiple special characters (more than 2)
    special_chars = re.findall(r'[!@#$%^&*()_+=\[\]{}/\|~<>;:.,?\"\'\\\+-]', text)
    if len(special_chars) > 2:
        return True

    return False
