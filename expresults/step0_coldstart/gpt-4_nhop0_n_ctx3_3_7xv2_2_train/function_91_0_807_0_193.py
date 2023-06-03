def is_spam(message):
    import re

    # Check for suspicious keywords in message
    spam_keywords = [
        "목표달성기념",
        "추천",
        "슈퍼개미",
        "수익",
        "부자",
        "노하우",
        "주식",
        "공부방",
        "이자",
        "카카오톡 오픈채팅방",
        "NBet",
        "첫 입",
        "첫 출",
        "무/한",
    ]
    
    for keyword in spam_keywords:
        if keyword in message:
            return True

    # Check for multiple consecutive special characters, generally found in spam messages
    if re.search(r"[!@#$%^&*(),.?\":{}/|<>]{2,}", message):
        return True
    
    # Check for url shorteners, common in spam messages
    url_shorteners = ["bit.ly", "goo.gl", "tinyurl.com", "t.co", "dlvr.it", "me2.kr", "opcn-kakao.com", "nbet02.com"]
    for shortener in url_shorteners:
        if shortener in message:
            return True

    # Check for a high number of percentages and/or money units, indicating a too-good-to-be-true deal
    percentage_count = len(re.findall(r"\d+%", message))
    money_count = len(re.findall(r"[£$€¥₩]\d+", message))
    if percentage_count + money_count >= 3:
        return True

    return False