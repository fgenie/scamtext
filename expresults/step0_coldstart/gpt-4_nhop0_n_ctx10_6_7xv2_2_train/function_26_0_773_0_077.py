def is_spam(message):
    import re
    
    # Check for short links
    if re.search(r'http[s]?://[a-zA-Z0-9]{,5}\.\w{,3}/[\w]+', message):
        return True

    # Check for percentage or amount of money
    if re.search(r'\d{1,2}%|\d{1,3}(,\d{3})*원', message):
        return True

    # Check for stock-related words
    if re.search(r'매집|상한가|증권사|종목', message):
        return True

    # Check for 단독 제휴 협약 or 인증번호
    if re.search(r'단독제휴협약|인증\d{4}', message):
        return True

    # Check for multiple special characters in a row
    if re.search(r'[_\-=+*!@\(\){}:;&\[\]]{2,}', message):
        return True

    return False