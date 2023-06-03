def is_spam(message: str) -> bool:
    import re

    # Check for spam keywords
    spam_keywords = ["체험", "VIP", "정보방", "증권사", "부장출신", "수익", "공시정보", "합병", "MOU", "체결", "확인", "분석", "추천", "실력", "입증"]
    for keyword in spam_keywords:
        if keyword in message:
            return True

    # Check for unusual URLs
    urls = re.findall(r'(https?://[^\s]+)', message)
    if urls:
        spam_tld = [".kr"]
        for url in urls:
            if any(tld in url for tld in spam_tld):
                return True

    # Check for unusual characters/text structure
    if "▼" in message or "▲" in message or "↑" in message or "↓" in message:
        return True

    # If no spam indicators are found, return False
    return False