def is_spam(message):
    import re

    # Check for spammy keywords or phrases
    spam_keywords = ['목표달성기념', '추천 디젠스', '차별화된 정보', '단독발표정보',
                     '상한가확정', '실력입증', '추천주', '체험반']

    for keyword in spam_keywords:
        if keyword in message:
            return True

    # Check for unusual amount of special characters or digits
    special_chars = re.findall(r'[^\w\s]+', message)
    digits = re.findall(r'\d+', message)

    if (len(special_chars) > 3 and len(digits) > 5):
        return True

    # Check for multiple URLS in the message
    urls = re.findall(r'https?://[\w\-.]+', message)
    if len(urls) > 1:
        return True

    return False