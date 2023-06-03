def is_spam(message):
    import re

    # List of spam keywords
    spam_keywords = ['당첨', '유료하지않습니다', '무료 입장', '장담합니다', '반등 구간 매매', '단체방', '증권', '지속적인 하락장', '수익', '성과']

    # Check if the message contains any spam keywords
    for keyword in spam_keywords:
        if keyword in message:
            return True

    # Check if the message has more than one URLs
    urls = re.findall(r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\\(\\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', message)
    if len(urls) > 1:
        return True

    return False