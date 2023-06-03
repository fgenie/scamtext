
import re

def is_spam(text):
    # Check for common spam keywords
    spam_keywords = [
        "단타매매",
        "하루 평균 수익",
        "환타",
        "일타강사진",
        "해.외.선.물."
    ]
    for keyword in spam_keywords:
        if keyword in text:
            return True

    # Check for short links
    short_link_patterns = [
        "https?:\/\/vvd.bz",
        "https?:\/\/me2.kr",
        "https?:\/\/bit.ly",
        "https?:\/\/goo.gl",
        "https?:\/\/tinyurl.com",
    ]
    for pattern in short_link_patterns:
        if re.search(pattern, text):
            return True

    # Check for weird/uncommon unicode characters
    if re.search(r"[\u2000-\u2cff]+", text):
        return True

    # Check for excessive punctuation
    if re.search(r"[\.,?!;:]{5,}", text):
        return True

    # If none of the above conditions are met, the message is not spam.
    return False
