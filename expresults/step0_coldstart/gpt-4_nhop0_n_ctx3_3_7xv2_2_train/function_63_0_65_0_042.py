def is_spam(message: str) -> bool:
    import re
    
    spam_keywords = ['출금', '종목', '매수세', '공시', '주식', '상승']
    keyword_count = 0

    for keyword in spam_keywords:
        if keyword in message:
            keyword_count += 1

    if keyword_count > 2:
        return True

    urls = re.findall('https?://(?:[-\w.]|(?:%[\da-fA-F]{2}))+', message)
    if len(urls) > 0 and "me2.kr" not in urls:
        return True

    return False