def is_spam(message: str) -> bool:
    import re

    # Check for common spam characteristics
    spam_patterns = [
        r"[0-9]+%",
        r"[0-9]+원",
        r"매[0-9]+%",
        r"승인전화X",
        r"무료수신거부",
        r"\(광고\)",
        r"https?:\/\/[^\s]+",
        r"체험",
        r"적중"
    ]

    for pattern in spam_patterns:
        if re.search(pattern, message):
            return True

    return False