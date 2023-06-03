def is_spam(message):
    """
    Determines if a message is spam or not based on some pre-defined keywords and patterns.
    
    :param message: str
    :return: bool
    """
    import re

    # Define keywords and patterns to detect spam
    spam_keywords = ['광고', '지원', '매수', '체험반', '수익', '투자', '최종논의단계', '코드', '무료거부', '특별혜택', '입장코드', '중개수수료']

    # Check if any spam keywords are in the message
    for keyword in spam_keywords:
        if keyword in message:
            return True
    
    # Check for http links and short url patterns
    urls = re.findall('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\\(\\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', message)
    short_urls = re.findall("https?://[^\s]+", message)
    
    if urls or short_urls:
        return True

    # None of the spam keywords and suspicious patterns were found in the message
    return False