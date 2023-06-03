def is_spam(message: str) -> bool:
    import re
    
    # Check for common spam phrases
    spam_phrases = ['축하합니다', '언론사 미공개', '극비 작전주', '적중', '목표달성기념', '추천주', '종목']
    for phrase in spam_phrases:
        if phrase in message:
            return True
    
    # Check for excessive amount of special characters
    special_chars = {'+', '!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '=', '|', '~', '`', ';', ':', '<', '>', '?', '/'}
    special_char_count = sum([1 for char in message if char in special_chars])
    if special_char_count > 5:
        return True

    # Check for URL pattern
    url_pattern = re.compile('https?://(?:[-\w.]|(?:%[\da-fA-F]{2}))+|me2.kr/[a-zA-Z0-9]+')
    urls = url_pattern.findall(message)
    if len(urls) > 1:
        return True

    return False