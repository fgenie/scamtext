def is_spam(message: str) -> bool:
    import re
    
    if not message:
        return False

    # Check for excessive use of symbols
    symbols = re.findall(r'[\W_]', message)
    if len(symbols) > len(message) * 0.5:
        return True

    # Check for uncommon url patterns
    spam_url_patterns = ["me2.kr", "url.kr", "openkakao.it", "http://ssg.li/"]
    for spam_url_pattern in spam_url_patterns:
        if spam_url_pattern in message.lower():
            return True

    # Check for advertisement and promotion keywords
    spam_keywords = ["%할인", "회원가입", "경품", "증정", "무료 체험", "4월파이널VIP체험반", "여의도4월체험반"]
    for spam_keyword in spam_keywords:
        if spam_keyword in message:
            return True

    # Check for new lines followed immediately by urls
    new_line_url = re.search(r'\nhttp', message)
    if new_line_url:
        return True

    # Check for excessive use of numbers
    numbers = re.findall(r'\d\d+', message)
    if len(numbers) > 6:
        return True

    return False