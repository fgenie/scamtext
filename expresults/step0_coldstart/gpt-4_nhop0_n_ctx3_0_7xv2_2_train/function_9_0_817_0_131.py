def is_spam(message: str) -> bool:
    import re
    
    # Checking for suspicious words indicating spam messages
    spam_words = ['목표달성기념', '추천', '상한가', '반입니다', 'AI사업본격화', 'C상장기업', 'MOU추친중']
    for word in spam_words:
        if word in message:
            return True
    
    # Checking for excessive usage of special characters
    special_characters = re.findall(r'[^a-zA-Z0-9가-힣\s]', message)
    if len(special_characters) > 5:
        return True
    
    # Checking for unusual URLs
    url_pattern = re.compile("https?://me2\.kr/[a-zA-Z0-9]*")
    url = re.findall(url_pattern, message)
    if len(url) > 0:
        return True

    return False