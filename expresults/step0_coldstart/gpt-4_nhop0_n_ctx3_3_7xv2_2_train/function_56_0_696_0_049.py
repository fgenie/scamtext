
import re

common_spam_keywords = [
    "광고",
    "성과안내",
    "약속",
    "참여 누적인원",
    "드리는 이 찬스",
    "운명",
    "점심 포장",
]

common_spam_patterns = [
    re.compile(r"http[s]?://\S+"),
]

def is_spam(message):
    message = message.lower()
   
    for keyword in common_spam_keywords:
        if keyword in message:
            return True

    for pattern in common_spam_patterns:
        if re.search(pattern, message):
            return True

    return False
