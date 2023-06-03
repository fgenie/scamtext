def is_spam(message):
    import re

    # Check for common spam keywords
    keywords = ['당신의 행복을', '돈이 있어야', '지금 바로 입장하세요', '안전거래소', '입장코드', '수익 실현', '광고', '지원금', '투자', '수수료', 'MOU추친중', '상한가']
    for keyword in keywords:
        if keyword in message:
            return True
    
    # Check for URLs
    url_pattern = re.compile(r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+')
    urls = re.findall(url_pattern, message)
    if len(urls) > 0:
        return True

    # Check for numbers followed by special characters or words
    patterns = ['[0-9]+\s*%[^ ]*', '[0-9]+\s*원[^ ]*', '[0-9]+\s*계약[^ ]*']
    for pattern in patterns:
        if re.search(pattern, message):
            return True

    return False