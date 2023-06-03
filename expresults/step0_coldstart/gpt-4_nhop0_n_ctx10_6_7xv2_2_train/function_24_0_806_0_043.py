def is_spam(message):
    import re

    # Check for common spam keywords
    spam_keywords = ['광고', '무료방매수', '신입', '종목', '바로가기', '선착', '네이버 주식', '익 절 가', '증권사', '알려드린', '적중']
    for keyword in spam_keywords:
        if keyword in message:
            return True

    # Check for typical spam URL patterns
    url_patterns = ['https?:\/\/\S+', 'bit\.ly\/\S+', 'dokdo\.in\/\S+', 'opcn-kakao\.com\/\S+', 'me2\.kr\/\S+']
    for pattern in url_patterns:
        if re.search(pattern, message):
            return True

    # Check for message containing only numbers or special characters
    if re.search('^[0-9\W]+$', message):
        return True

    return False