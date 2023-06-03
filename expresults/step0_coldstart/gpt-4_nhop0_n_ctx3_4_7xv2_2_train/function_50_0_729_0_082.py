def is_spam(message):
    import re
    
    spam_keywords = ['광고', '입장코드', '무료참여', '무료거부', '선물거래', '클릭', '도배']

    # Check for spam keywords
    for keyword in spam_keywords:
        if keyword in message:
            return True

    # Check for URLs
    url_pattern = re.compile(r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\\(\\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+')
    urls = re.findall(url_pattern, message)
    if len(urls) > 0:
        return True

    # Check for excessive use of special characters
    special_chars_pattern = re.compile(r'[^a-zA-Z0-9가-힣\s]')
    special_chars = re.findall(special_chars_pattern, message)
    if len(special_chars) > len(message) / 2:
        return True

    return False