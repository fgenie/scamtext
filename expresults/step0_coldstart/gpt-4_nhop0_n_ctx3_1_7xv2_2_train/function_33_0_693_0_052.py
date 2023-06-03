def is_spam(text: str) -> bool:
    import re

    # List of spam-related keywords
    spam_keywords = ['적중', '통합운영', '제한참여', '혜택유지', 'VIP', '투자체험', '매수', '매도', '타점', '시황', '뉴스공유', '추천종목']

    # Check for excessive use of special characters
    special_chars = ['!', '@', '#', '$', '%', '&', '*']
    special_char_count = sum(text.count(char) for char in special_chars)
    if special_char_count > len(text) * 0.2:
        return True

    # Check for suspicious URLs (using regex)
    suspicious_url_pattern = re.compile(r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\\(\\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+')
    if suspicious_url_pattern.search(text) is not None:
        return True

    # Check for spam keywords
    for keyword in spam_keywords:
        if keyword in text:
            return True

    return False