
import re

def is_spam(message):
    # Check for URL shorteners
    if re.search(r"http(s)?://(me2\.kr|bit\.ly|goo\.gl|tinyurl\.com|t\.co)/\S+", message):
        return True

    # Check for percentage signs and Korean currency symbols
    if re.search(r"(\d+%↑|원)", message):
        return True

    # Check for any special characters and Korean words that might indicate spam
    if re.search(r"[*]|(선물지수 프로젝트|추천주 현황|입장가능합니다|돌파)", message):
        return True

    return False
