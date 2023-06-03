def is_spam(message: str) -> bool:
    import re

    # Check for spam keywords
    spam_keywords = [
        '안내',
        '추천',
        '만원',
        '십만원',
        '장 시작전',
        '정부기관',
        '종목'
    ]

    for keyword in spam_keywords:
        if keyword in message:
            return True

    # Check for suspicious URLs
    url_pattern = re.compile('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\\(\\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+')
    urls = re.findall(url_pattern, message)
    
    if len(urls) > 0:
        # Check if the URL has a suspicious domain
        suspicious_domains = [
            'vvd.bz',
            'me2.kr',
        ]

        for url in urls:
            for domain in suspicious_domains:
                if domain in url:
                    return True

    return False