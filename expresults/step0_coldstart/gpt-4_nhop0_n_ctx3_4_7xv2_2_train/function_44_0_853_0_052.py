
import re

def is_spam(message: str) -> bool:
    spam_patterns = [
        r"\b신청[^가-힣]*", 
        r"\b입장[^가-힣]*", 
        r"\b(?:https?://|www\.)[^\s]*", 
        r"\b(?:[A-Za-z0-9_]{2,}\.)+[a-zA-Z]{2,6}\b"
    ]

    message = re.sub(r"\s+", " ", message)

    for pattern in spam_patterns:
        if re.search(pattern, message):
            return True
    return False
