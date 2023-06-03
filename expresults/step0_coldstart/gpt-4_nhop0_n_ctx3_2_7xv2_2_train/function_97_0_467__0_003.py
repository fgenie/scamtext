def is_spam(message: str) -> bool:
    import re
    
    # Spam patterns
    spam_patterns = [
        r"지니틱스, 나노 수익",
        r"안전하고 확률 높은 종목만 선별",
        r"정회원방 입장"
    ]
    
    # Search for spam patterns
    for pattern in spam_patterns:
        if re.search(pattern, message):
            return True

    # Check for suspicious URLs
    url_pattern = r'(https?:\/\/(?:www\.|(?!www))[a-zA-Z0-9][a-zA-Z0-9-]+[a-zA-Z0-9]\.[^\s]{2,}|www\.[a-zA-Z0-9][a-zA-Z0-9-]+[a-zA-Z0-9]\.[^\s]{2,}|https?:\/\/(?:www\.|(?!www))[a-zA-Z0-9]+\.[^\s]{2,}|www\.[a-zA-Z0-9]+\.[^\s]{2,})'
    urls = re.findall(url_pattern, message)
    if len(urls) > 0:
        if re.search(r'(me2\.kr|opcn-kakao\.com)', urls[0]):
            return True

    return False