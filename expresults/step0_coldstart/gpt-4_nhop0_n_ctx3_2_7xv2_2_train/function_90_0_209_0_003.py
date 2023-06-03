def is_spam(message: str) -> bool:
    import re

    keywords = ["상한가", "공시발표", "달성", "참여하기", "매집단계", "월 이후"]
    spam_phrases = [r"(\d+)퍼.센.트"]
    short_url_patterns = [r"https?:\/\/[^\s]*\.(?:me2|vo)\.(?:kr|la)\/[^\s]+"]

    # Check if any keywords exist in the message
    if any(keyword in message for keyword in keywords):
        return True

    # Check if any spam phrases exist in the message
    for phrase in spam_phrases:
        if re.search(phrase, message):
            return True

    # Check for short URLs
    for pattern in short_url_patterns:
        if re.search(pattern, message):
            return True

    return False