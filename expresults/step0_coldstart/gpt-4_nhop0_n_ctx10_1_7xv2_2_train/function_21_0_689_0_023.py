def is_spam(message: str) -> bool:
    import re
    
    # Patterns to detect spam messages
    spam_patterns = [
        r'(광고)',
        r'(무료거부)',
        r'https?://\S{5,}',
        r'목표가:.+\d+',
        r'오픈네이버',
        r'무료방매수사인',
        r'엠바고',
        r'TG그룹_선물정보',
        r'(최소\d+연상)',
    ]
    
    # Check if any of the patterns match the input message
    for pattern in spam_patterns:
        if re.search(pattern, message):
            return True
            
    # If none of the patterns match, return False (not spam)
    return False