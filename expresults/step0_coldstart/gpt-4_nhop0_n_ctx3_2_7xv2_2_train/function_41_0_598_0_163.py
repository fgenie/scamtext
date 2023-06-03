def is_spam(message):
    import re

    # Check for excessive capitalization
    if len(re.findall(r'[A-Z]', message)) > 0.5 * len(message):
        return True

    # Check for common spam words/phrases
    spam_keywords = [
        "목표달성기념",
        "추천 디젠스",
        "투자동호회",
        "선물 거래",
        "미시적 관점",
        "성공의 그림",
        "동기부여",
        "무료거부",
        "입장가능",
        "vvip",
        "프로젝트",
        "인증번호",
    ]
    if any(keyword in message for keyword in spam_keywords):
        return True

    # Check for excessive use of special characters
    if len(re.findall(r'[!@#$%^&*(),.?":{}|<>~`_]', message)) > 0.25 * len(message):
        return True

    # Check for excessive consecutive white spaces
    if re.search(r"\s\s+", message):
        return True

    return False