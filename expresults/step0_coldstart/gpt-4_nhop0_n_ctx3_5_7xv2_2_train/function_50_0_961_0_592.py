def is_spam(text):
    import re
    
    # Check for unusual amount of special characters or numbers
    special_chars = re.findall(r'[^\w\s]', text)
    if len(special_chars) / len(text) > 0.25:
        return True

    # Check for URLs, especially short URLs (me2.kr, bit.ly, etc.)
    urls = re.findall(r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\\(\\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', text)
    short_urls = re.findall(r'(?:me2\.kr|bit\.ly)/[\w]+', text)
    if len(urls) > 2 or len(short_urls) > 0:
        return True

    # Check for unusual consecutive characters (like "!!!!!!!!")
    consecutive_chars = re.findall(r'([a-zA-Z0-9!@#\$%\^&\*])\1{3,}', text)
    if len(consecutive_chars) > 0:
        return True
        
    # Check for non-Korean and non-English language
    non_korean_english = re.findall(r'[^\uAC00-\uD7A3\sA-Za-z]', text)
    if len(non_korean_english) > 0:
        return True

    # Check for common spam phrases
    spam_phrases = [
        "특별찬스잡으세요", "전달받은 고급 정보", "무료수신거부", 
        "인증번호",
        "대형", "건강", "이벤트", "사은품", " 최소 150%"
    ]
    for phrase in spam_phrases:
        if phrase in text:
            return True

    # If none of the above conditions are met, it's not spam
    return False