def is_spam(message: str) -> bool:
    import re

    # Check for common spam phrases
    spam_phrases = [
        "다른곳 비교불가",
        "지난주 추천주",
        "발표예정정보",
        "월공개",
        "F상장기업",
        "카카오톡제재",
        "악성광고",
        "텔레그램으로 이동"
    ]

    for phrase in spam_phrases:
        if phrase in message:
            return True

    # Check for excessive use of special characters
    special_chars = re.findall(r"[~!@#$%^&*]", message)
    if len(special_chars) > 5:
        return True

    # Check for URLs
    urls = re.findall(r"http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+", message)
    if len(urls) > 0:
        return True

    return False