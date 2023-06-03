def is_spam(message: str) -> bool:
    import re
    
    # Check for common spam keywords in the message
    spam_keywords = ['추천주', '마감', '프로', 'VIP', '실력입증', '참여', '차별화된', '연혁', '체험반', '도움']
    for keyword in spam_keywords:
        if keyword in message:
            return True
    
    # Check for suspicious URLs (shortened URLs, non-standard domains)
    if re.search(r'https?://(?:[a-z0-9-_]+\.)+[a-z]{2,}(/[a-zA-Z0-9()@:%_\+.~#?&//=]*)?', message):
        return True

    # Check for unusual capitalization (uppercase letters in the middle of a sentence)
    if re.search(r'\b[A-Z0-9]+\b', message):
        return True

    return False