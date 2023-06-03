def is_spam(message):
    import re

    # Check for the presence of URLs
    urls = re.findall(r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\\(\\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', message)
    if len(urls) > 0:
        return True

    # Check for the presence of financial keywords or symbols
    financial_keywords = ['↑', '돌파', '추천주', '체험반', '다음주', '종료', '증가']
    for keyword in financial_keywords:
        if keyword in message:
            return True

    # Check for the presence of unusual characters and patterns
    unusual_patterns = [
        re.compile(r'[ㄱ-ㅎㅏ-ㅣ]{2,}'),
        re.compile(r'[!@#$%^&*(),.?":{}|<>]{3,}')
    ]
    for pattern in unusual_patterns:
        if pattern.search(message) is not None:
            return True

    # Check for a large number of digits
    digits = re.findall(r'\d+', message)
    if len(digits) > 2:
        return True

    return False