def is_spam(message):
    import re
    
    # List of spam keywords
    spam_keywords = [
        '광고', '신청', '개설', '입장', '소통', '수익', '안내', '단투', '정보', '무료', '주식',
        '원칙', '가격', '노하우', '지속', '최고', '투자', '지식', '인사이트', '부자', '거부'
    ]

    # Check for presence of URL
    url_pattern = re.compile(r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\\(\\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+')
    has_url = bool(url_pattern.search(message))

    # Check for excessive use of special characters
    special_chars_pattern = re.compile(r"[!@#$%^&*(),.?\":{}|<>]")
    special_chars_count = len(special_chars_pattern.findall(message))
    excessive_special_chars = special_chars_count / len(message) > 0.1

    # Check for presence of spam keywords
    has_spam_keywords = any(keyword in message for keyword in spam_keywords)

    return has_url or excessive_special_chars or has_spam_keywords