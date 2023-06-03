
import re

def is_spam(text):
    # Check for typical spam expressions
    spam_expressions = [
        "(광고)",
        "▼참여하기▼",
        "무료수신거부",
        "▶다.올.인.베.스.트.먼.트",
        "▶가.온.칩.스",
        "▼클릭",
        "잔여",
        "▶대.모",
        "%",
    ]
    
    # Check for presence of shortened URLs
    url_regex = r"(?:https?:\/\/me2\.kr\/[A-z0-9]+|https?:\/\/vo\.la\/[A-z0-9]+)"

    if any(re.search(expression, text) for expression in spam_expressions) or re.search(url_regex, text):
        return True

    return False
