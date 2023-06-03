def is_spam(message):
    import re
    
    spam_keywords = ['축하합니다', '힘든시기', '당첨', 'AI사업본격화', '단독제휴협약', '막바지', '상한가', '목표달성기념', '추천', '디젠스']
    url_pattern = r'https?://(?:[-\w.]|(?:%[\da-fA-F]{2}))+'

    # Check for spam keywords
    for keyword in spam_keywords:
        if keyword in message:
            return True

    # Check for URLs
    urls = re.findall(url_pattern, message)
    if urls:
        return True

    return False