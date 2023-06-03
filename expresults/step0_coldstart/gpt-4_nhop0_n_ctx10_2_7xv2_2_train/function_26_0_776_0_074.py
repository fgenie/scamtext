def is_spam(message: str) -> bool:
    # List of common spam keywords
    spam_keywords = [
        "종목", "수익률", "추천주", "%↑", "무료수신거부", "투자", "진행", "무료배송", "할인",
        "특가", "소식", "주식회사", "최저가", "최대", "영업점", "체험반",
    ]

    # Check if any spam keyword in the message
    for keyword in spam_keywords:
        if keyword in message:
            return True

    # Check if message contains URL(s)
    if "http://" in message or "https://" in message or "www." in message:
        return True

    return False