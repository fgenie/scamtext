def is_spam(message: str) -> bool:
    import re

    # Check for common spam words and phrases
    spam_phrases = [
        r"실력보셨죠",
        r"목요일 오늘 회사공시 발표",
        r"최소 금요일 20%",
        r"적중하여 좋은결과",
        r"(?=.*클릭)(?=.*종목확인)",
        r"익 절 가",
        r"능적수익률",
    ]

    for phrase in spam_phrases:
        if re.search(phrase, message):
            return True

    # Check for suspicious URLs
    if re.search(r"https:\/\/opcn-kakao\.com\/[a-zA-Z0-9]*", message):
        return True

    return False