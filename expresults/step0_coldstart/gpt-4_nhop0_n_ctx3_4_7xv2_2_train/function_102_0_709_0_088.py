
import re

def is_spam(message):
    message = message.lower()
    
    # Checking for excessive special characters
    special_chars = re.findall(r'[^a-zA-Z0-9가-힣\s]', message)
    if len(special_chars) > len(message) * 0.4:
        return True

    # Checking for URL shorteners
    short_url = re.findall(r'(?:https?://|www\.|bit\.ly)(?:[^\s])+', message)
    if short_url:
        return True

    # Checking for suspicious keywords
    keywords = ["국내식약처", "발표", "적립금", "에이피", "엠바고", "리뉴얼"]
    for keyword in keywords:
        if keyword in message:
            return True

    return False
