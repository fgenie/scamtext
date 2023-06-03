def is_spam(message: str) -> bool:
    import re

    # Check for spam-related keywords in message
    spam_keywords = ["당첨", "투자", "수익", "비공개정보방", "단체방", "매수매도타점공유"]
    for keyword in spam_keywords:
        if keyword in message:
            return True

    # Check for url patterns that typically appear in spam messages
    urls_in_message = re.findall(r"https?://[^\s]+", message)
    spam_url_patterns = ["me2.kr"]
    for url in urls_in_message:
        for pattern in spam_url_patterns:
            if pattern in url:
                return True

    # Check for consecutive capital letters, numbers, or symbols
    consecutive_pattern = re.compile(r"([A-Z0-9!@#$%&*+=()\\^~_-]{5,})")
    if consecutive_pattern.search(message):
        return True

    # If none of the conditions above are met, return False (not spam)
    return False