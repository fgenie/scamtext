def is_spam(message: str) -> bool:
    import re
    
    spam_indicators = [
        r'\d{1,3}(?:,\d{3})*(?:\.\d{2})?',
        r'\.{0,1}[a-zA-Z]+(\.[a-zA-Z]+)+',
        r'%|\+',
        r'\d[,\.]\d',
        r'종목',
        r'출금',
        r'수익',
        r'투자',
    ]

    normal_indicators = [
        r'(하이|안녕|반가워)',
        r'ㅎ[ㅣ]*ㅇ',
    ]

    for indicator in normal_indicators:
        if re.search(indicator, message):
            return False

    count_spam_indicators = 0
    for indicator in spam_indicators:
        if re.search(indicator, message):
            count_spam_indicators += 1

    if count_spam_indicators >= 2:
        return True

    return False