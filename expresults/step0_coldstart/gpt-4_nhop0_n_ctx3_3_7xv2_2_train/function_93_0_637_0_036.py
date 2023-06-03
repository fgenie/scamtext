
import re

def is_spam(message):
    # Identify spam patterns
    patterns = [
        r"\d{1,2}월마지막안내",
        r"\d{1,2}일추천주",
        r"(?:http|https)://(?:[\w]+(?:(?:\.|-)[\w]+)*(?:\.(?:\w{2,5})))?",
        r"만원한장 시작",
        r"십만원 만들기",
        r"신 청 하 신",
        r"입장 안내 드립니다"
    ]

    for pattern in patterns:
        match = re.search(pattern, message)
        if match:
            return True
    return False
