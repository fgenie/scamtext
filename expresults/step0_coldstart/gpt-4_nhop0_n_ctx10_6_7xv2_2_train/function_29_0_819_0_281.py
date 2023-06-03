def is_spam(message):
    import re
    
    # Check for common spam indicators
    spam_patterns = [
        r'\(광고\)',
        r'https?:\/\/[^\s]+',
        r'\d{1,2}시부터|오늘오후|오늘밤',
        r'상한가|수익률|투자|프로젝트|추천|실적|매매',
        r'무료거부|무료수신거부'
    ]
    
    for pattern in spam_patterns:
        if re.search(pattern, message):
            return True

    # Check for excessive use of special characters
    special_chars = '!@#$%^&*()_-+=[]{}|;<>?/'
    special_count = sum(1 for char in message if char in special_chars)

    if special_count / len(message) > 0.05:
        return True

    return False