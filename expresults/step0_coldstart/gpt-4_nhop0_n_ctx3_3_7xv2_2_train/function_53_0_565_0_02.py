def is_spam(message):
    import re

    message = message.lower()

    # Check for spam keywords
    spam_keywords = ['발표', '엠바고', '정식허가', '최소', '긴급입수', '국내식약처', '국내', '정식허가', '상한가', '파이널', '체험반', '공시발표', '단독입수']
    for keyword in spam_keywords:
        if keyword in message:
            return True

    # Check for url shortened links
    url_patterns = [
        r'https?://bit\.ly/\S+',
        r'https?://me2\.kr/\S+',
    ]
    for pattern in url_patterns:
        if re.search(pattern, message) is not None:
            return True

    # Return false if none of the spam criteria above is met
    return False