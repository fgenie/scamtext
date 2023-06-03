def is_spam(message):
    import re
    
    # Lowercase the message
    message = message.lower()

    # Check for spam keywords
    spam_keywords = ['추천', '상한가', '모아', '공시정보', '돌파', '체험반', '계약', '지원금', '최대', '무료거부', '출발', '바로가기']
    for keyword in spam_keywords:
        if keyword in message:
            return True

    # Check for multiple exclamation points
    if re.search(r'!{2,}', message):
        return True
        
    # Check for urls with suspicious domain extensions
    url_pattern = re.compile(r'https?://\S+(?=\s|$)')
    urls = url_pattern.findall(message)
    spam_domains = ['.kr/', '.la/', '.ru/', '.ly/']
    for url in urls:
        if any(domain in url for domain in spam_domains):
            return True

    # Check if there are numeric values followed by % (example: 20%)
    if re.search(r'\d+%', message):
        return True

    # Check for a combination of 4 or more digits and alphabets consecutively
    if re.search(r'(?:(?:\d|\D){4,})', message):
        return True

    return False