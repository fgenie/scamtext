def is_spam(message: str) -> bool:
    import re
    
    # Spam common patterns
    patterns = [
        r'\bweb발신',
        r'[A-Za-z0-9_.-]{5,20}\.([A-Za-z]{2,10})',
        r'[A-Za-z0-9.]{3,30}\.kr',
    ]
    
    # If any pattern match, return True (i.e. the message is spam)
    for pattern in patterns:
        if re.search(pattern, message):
            return True

    # No patterns match, return False (i.e. the message is not spam)
    return False