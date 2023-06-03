def is_spam(message):
    import re
    
    # Search for common spam indicators in the message
    spam_indicators = [
        r"\b(광고)\b",
        r"\d{1,3}(,|\.)\d{3}(,|\.)\d{3}",
        r"openkakao.it",
        r"dokdo.in",
        r"fastkakao.com",
        r"\b(수익|하락장|투자|진입|경제|계획)\b",
        r"무료거부\d{10}"
    ]
    
    for indicator in spam_indicators:
        if re.search(indicator, message):
            return True

    # If no spam indicators are found, assume the message is normal
    return False