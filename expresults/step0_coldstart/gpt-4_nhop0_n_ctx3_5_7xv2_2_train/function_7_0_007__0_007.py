
import re

def is_spam(message: str) -> bool:
    spam_keywords = ['퍼.센.트', '월 천', '업실현', '다.올.인.베.스.트.먼.트', '가.온.칩.스', '대.모', '정보의', '월공개']
    spam_patterns = ['\d{4} 코리아빌드위크', '전시소개', '전시명']

    # Check if the message contains any spam keywords
    for keyword in spam_keywords:
        if keyword in message:
            return True

    # Check if the message contains any spam patterns
    for pattern in spam_patterns:
        if re.search(pattern, message):
            return True

    # If none of the spam indicators are found, the message is considered normal
    return False
