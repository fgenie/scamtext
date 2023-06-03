def is_spam(message: str) -> bool:
    import re
    
    # Spam indicators
    spam_keywords = ['(광고)', 'EVENT', '지원금', '혜택', '종목', '수익', '주식', '해외선물', '무료거부']
    url_pattern = r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+'

    # Check if the message contains keywords
    for keyword in spam_keywords:
        if keyword in message:
            return True

    # Check if the message contains a URL
    urls = re.findall(url_pattern, message)
    if len(urls) > 0:
        return True

    return False