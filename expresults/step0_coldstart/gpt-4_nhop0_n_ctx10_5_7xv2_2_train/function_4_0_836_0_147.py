
import re

def is_spam(message):
    spam_keywords = [
        "VIP", "체험반", "수익", "주식", "공시발표", "케이공간", "슈퍼개미", "노하우", "카카오톡",
        "오픈채팅방", "vvip", "루멘스", "회원님", "실력입증", "월 천", "고정수입", "미야",
        "입장", "안내", "한농화성", "임베디드", "정밀", "월 천", "입", "출"
    ]

    # Check for URLs
    url_pattern = r"http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\\(\\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+"
    urls = re.findall(url_pattern, message)
    if len(urls) > 0:
        return True

    # Check for any keywords in the message
    message_lower = message.lower()
    for keyword in spam_keywords:
        if keyword.lower() in message_lower:
            return True

    # If no keywords or URLs are matched, it's not spam
    return False
