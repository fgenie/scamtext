
import re

def is_spam(message):
    # Check for URL shorteners
    url_shorteners = ['me2.kr']
    for url in url_shorteners:
        if url in message:
            return True

    # Check for excessive repetitive characters
    repetition = re.findall(r"(\w)\1{2,}", message)
    if repetition:
        return True

    # Check for long continuous strings that might be stock codes
    long_string = re.findall(r"[A-Za-z가-힣0-9]{10,}", message)
    if long_string:
        return True

    # Check for atypical percentage symbols
    if "↑" in message or "↓" in message:
        return True

    return False
