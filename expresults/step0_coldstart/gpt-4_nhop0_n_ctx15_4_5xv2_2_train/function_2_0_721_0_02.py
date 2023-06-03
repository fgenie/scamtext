
import re

def is_spam(message):
    # Keywords and phrases often found in spam messages
    spam_keywords = [
        "무료", "출금", "적중", "상품목록", "기대 성과", "지급중", 
        "상한가", "성공현황", "성과 보여드리고", "공지", "추천"
    ]

    # Patterns often found in scam URLs
    scam_url_patterns = [
        r"(?i)bit\.ly",
        r"(?i)me2\.kr"
    ]

    # Checking if any spam keyword is found in the message
    for keyword in spam_keywords:
        if keyword in message:
            return True

    # Checking if any scam URL pattern is found in the message
    for pattern in scam_url_patterns:
        if re.search(pattern, message):
            return True

    # If none of the spam indicators are found, the message is considered normal
    return False
