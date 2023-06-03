
import re


def is_spam(message: str) -> bool:
    spam_keywords = [
        "무료거부",
        "프로젝트",
        "지원금",
        "특별",
        "혜택",
        "상승",
        "수익",
        "웹그룹",
        "광고",
        "초대",
        "폭등"
    ]

    normal_keywords = [
        "안녕하세요",
        "하루",
        "이제",
        "문의",
        "수고",
        "회의",
        "친구",
    ]
    
    message = message.lower().strip()
    
    spam_count = 0
    normal_count = 0

    # Count spam keywords in the message
    for keyword in spam_keywords:
        if keyword in message:
            spam_count += 1

    # Count normal keywords in the message
    for keyword in normal_keywords:
        if keyword in message:
            normal_count += 1
    
    if spam_count > normal_count:
        return True
    
    return False
