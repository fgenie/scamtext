def is_spam(message):
    import re
    
    # Check for typical spam keywords
    spam_keywords = ['상한가', '종목', '추천주', '광고', '환수', '계좌', '수익률', '입수정보', '정식허가']
    for word in spam_keywords:
        if word in message:
            return True

    # Check for short links
    short_links = re.findall("https?://(?:\w{2}\.)([a-zA-Z0-9]+)\.([a-zA-Z]+)/?(\w*[a-z0-9_-]+)?", message)
    if short_links:
        return True

    # Check for 고객상담센터 like numbers
    customer_center_numbers = re.findall(r"(?:고객[^\w]?|상담[^\w]?)센터[^\w]? ?(?:\d{4}[- ]\d{4})", message)
    if customer_center_numbers:
        return False

    # Check for 거부문구 or 무료거부 like texts
    reject_keywords = ['무료거부', '번호:', '선착:', '거부문구']
    for keyword in reject_keywords:
        if keyword in message:
            return True

    # Check for an excessive use of special characters
    special_chars = re.findall(r"[\*|\/\/|\(\)\.]", message)
    if len(special_chars) > 3:
        return True

    return False