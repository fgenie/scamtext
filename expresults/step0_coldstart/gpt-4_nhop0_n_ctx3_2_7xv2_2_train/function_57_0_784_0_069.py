def is_spam(message):
    import re

    keywords = ['광고', '투자', '핵심 기법', '수익률', '분석', '증권사', '무료수신거부', '체험반', '추천']
    url_pattern = re.compile(r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+')
    
    # Check if message contains spam keywords
    for keyword in keywords:
        if keyword in message:
            return True

    # Check for URL patterns in message
    urls = url_pattern.findall(message)
    if len(urls) > 0:
        return True

    return False