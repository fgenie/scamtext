
import re

def is_spam(message):
    # Check for common spam phrases
    spam_phrases = [
        r"수익달성",
        r"수익 방법",
        r"지금 바로",
        r"행운의 기회",
        r"행복을그리다",
        r"최대수혜주",
        r"지원받고",
        r"투자 노하우",
        r"돌파",
        r"한농화성",
        r"주식 공부방",
        r"무료 강습"
    ]

    for phrase in spam_phrases:
        if re.search(phrase, message, re.IGNORECASE):
            return True

    # Check for shortened URLs
    url_patterns = [
        r"https?:\/\/(?:www\.|bit\.ly|me2.kr|buly.kr|r1ch.co|ko.gl)\/\S+"
    ]

    for pattern in url_patterns:
        if re.findall(pattern, message, re.IGNORECASE):
            return True

    # Check for excessive use of special characters
    special_chars = r"[!@#$%^&*(),.?\":{}|<>]+"

    # Count special characters
    count = len(re.findall(special_chars, message))
    if count / len(message) > 0.15:
        return True

    return False
