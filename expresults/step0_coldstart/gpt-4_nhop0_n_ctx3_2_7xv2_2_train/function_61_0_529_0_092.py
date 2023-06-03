def is_spam(message: str) -> bool:
    import re
    
    # Check for typical spam keywords and patterns
    spam_keywords = ['배당', '선물지급', 'VIP투자', '상한가', '단독발표', '프로모션', '그룹', '사업본격화', '상장기업', 'MOU추친중', '실력으로 입증', '차별화 된 분석']
    for keyword in spam_keywords:
        if keyword in message:
            return True
    
    # Check for URL shortener services
    url_shorteners = ['me2.kr']
    for shortener in url_shorteners:
        if shortener in message:
            return True
    
    # Check for repeated special characters, which may indicate a suspicious message
    if re.search(r"([!?.])\1{1,}", message):
        return True

    return False