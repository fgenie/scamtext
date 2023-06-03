def is_spam(message):
    import re

    spam_keywords = [
        "주식",
        "증권",
        "체험반",
        "추천주",
        "종목",
        "VIP",
        "정보",
        "수익률",
        "무료",
        "판매",
        "계좌",
        "공개",
        "분석",
        "상승",
        "광고",
        "최근",
        "금전",
        "요구",
        "다름이 아니라",
    ]

    message_lower = message.lower()

    # If there is a URL in the message
    if re.search(r"(https?://\S+)|(www\.\S+)", message_lower):
        return True

    # Check if any of the spam keywords appear in the message
    for keyword in spam_keywords:
        if keyword in message_lower:
            return True

    return False