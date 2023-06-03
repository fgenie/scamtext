def is_spam(message):
    import re

    # Check for suspicious words indicating spam
    spam_words = ['FDA승인', '임상3상완료', '정부지원', '신약개발', '진입', '추천주', '꿀팁', '비결', '안내']
    for word in spam_words:
        if word in message:
            return True

    # Check for suspicious URL patterns
    suspicious_url_patterns = [r'https?:\/\/\S+', r'me2\.kr\/\S+']
    for pattern in suspicious_url_patterns:
        if re.search(pattern, message):
            return True

    # Check for percentage signs and currency symbols
    if re.search(r'[\d%]+', message) and any(char in message for char in ['$', '₩', '€', '£', '¥']):
        return True

    return False