
import re

def is_spam(message):
    message = message.lower()

    spam_keywords = [
        "추천", "전용", "당첨", "maje", "\.com",
        "계열", "알려드린", "카지노", "이벤트",
        "출금", "입금", "양도", "적립금"
    ]

    for keyword in spam_keywords:
        if re.search(keyword, message):
            return True

    return False
