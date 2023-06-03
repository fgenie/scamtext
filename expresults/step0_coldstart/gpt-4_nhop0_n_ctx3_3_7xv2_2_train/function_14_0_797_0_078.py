def is_spam(message):
    import re

    # Spam keywords and patterns
    spam_keywords = [
        r"매수",
        r"회수 증정",
        r"공짜",
        r"추천",
        r"세력",
        r"이벤트",
        r"증정",
        r"무료",
        r"수익",
        r"보상",
        r"금전적 요구",
        r"배당",
        r"보장",
        r"약속",
        r"당첨",
    ]

    spam_patterns = [
        r"https?://[^ ]*",
        r"0[0-9]{9}",  # phone number pattern with 10 digits starting with 0
        r"㈜|\(주\)",  # company prefix symbols
        r"공시발표",
    ]

    # Check for presence of spam keywords or patterns in the message
    for keyword in spam_keywords:
        if re.search(keyword, message):
            return True

    for pattern in spam_patterns:
        if re.search(pattern, message):
            return True

    return False