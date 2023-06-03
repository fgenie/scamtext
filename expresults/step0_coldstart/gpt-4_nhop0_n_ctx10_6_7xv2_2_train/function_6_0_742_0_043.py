def is_spam(message: str) -> bool:
    import re

    # Check for common spam message phrases
    spam_phrases = [
        "클릭",
        "무료",
        "상한가확정",
        "바로가기",
        "매일 웃",
        "월 천 고정수입",
        "해선투자동호회",
        "모투대회무료참여",
        "증권",
        "선물",
        "Coin",
    ]

    if any(phrase in message for phrase in spam_phrases):
        return True

    # Check for url-like patterns
    url_pattern = re.compile(r"http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*'\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+")
    url_match = re.findall(url_pattern, message)

    if url_match:
        return True

    # Check for potential phone numbers
    phone_pattern = re.compile(r'(\d{2,4}-\d{2,4}-\d{2,4})')
    phone_match = re.findall(phone_pattern, message)

    if phone_match:
        return True

    return False