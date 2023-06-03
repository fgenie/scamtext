def is_spam(message):
    import re

    spam_indicators = [
        r"\b(광고)\b",
        r"\b(해선투자동호회)\b",
        r"\b(일베에 다\n)|(공작 이다)\b",
        r"\b(무료거부)\b",
        r"\b(입장코드)\b",
    ]

    normal_indicators = [
        r"\[(당근페이)\]",
        r"\[인증번호\]"
    ]

    for indicator in normal_indicators:
        if re.search(indicator, message, re.IGNORECASE):
            return False

    for indicator in spam_indicators:
        if re.search(indicator, message, re.IGNORECASE):
            return True

    # If none of the specific patterns were found, classify as normal
    return False