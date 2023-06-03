def is_spam(message: str) -> bool:
    import re

    # Check for spammy features in the message
    spam_indicator_patterns = [
        r"(현재가대비|최종논의단계|당일공개|폭등확정)",
        r"(https?://[^\s]+)",
        r"(축하합니다|세토피아|모레 공시발표)",
        r"\d{1,2}일"
    ]
    
    normal_indicator_patterns = [
        r"(나는\s뭐먹고\s살아야되노)",
        r"(지난주\s추천주\s현황)",
        r"(정보하나\s준다)"
    ]

    # Check for spam patterns using regular expressions
    for pattern in spam_indicator_patterns:
        if re.search(pattern, message):
            return True

    # Check for normal patterns using regular expressions
    for pattern in normal_indicator_patterns:
        if re.search(pattern, message):
            return False

    # If no clear indication is found, assume the message is not spam
    return False