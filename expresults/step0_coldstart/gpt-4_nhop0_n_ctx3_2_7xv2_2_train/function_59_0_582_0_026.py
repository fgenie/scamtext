def is_spam(message: str) -> bool:
    # Common spam keywords
    spam_keywords = ["VIP", "공시", "체험", "단독", "광고", "텔레그램", "제재", "혜택", "처음", "받아보세요", "추천", "안내", "잠금해제", "한정", "세토피아", "어림", "거래"]

    # If message contains too many capital letters 
    if sum(1 for c in message if c.isupper()) > len(message) * 0.3:
        return True

    # If message contains short URLs
    if "me2.kr" in message or "bit.ly" in message:
        return True

    # If message contains at least 3 spam keywords
    if sum(1 for keyword in spam_keywords if keyword in message) >= 3:
        return True

    return False