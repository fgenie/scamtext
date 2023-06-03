def is_spam(message: str) -> bool:
    import re
    
    # Check for shortened URLs
    short_url_pattern = 'https?://\S*(?:bit.ly|me2.kr)\S*'
    if re.search(short_url_pattern, message):
        return True

    # Check for special characters
    special_characters = ['+','%', '⏪']
    for char in special_characters:
        if char in message:
            return True

    # Check for promotion and discount keywords
    keywords = ['보증', '매수', '요율', '초대', '이벤트']
    if any(keyword in message for keyword in keywords):
        return True
        
    return False