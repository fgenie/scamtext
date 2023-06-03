def is_spam(message: str) -> bool:
    import re

    # Check for suspicious keywords in the message
    keywords = ["초대", "수익", "체험반", "정확한 분석", "검증된 수익률", "종목상담", "추천"]
    for keyword in keywords:
        if keyword.lower() in message.lower():
            return True

    # Check for URLs with suspicious patterns in the message
    url_pattern = re.compile(r'(http[s]?://[^\s]+)')
    urls = re.findall(url_pattern, message)    
    for url in urls:
        if (re.search(r'me2\.kr', url)):
            return True

    # If the message doesn't contain any suspicious keywords or patterns,
    # assume it is a normal message
    return False