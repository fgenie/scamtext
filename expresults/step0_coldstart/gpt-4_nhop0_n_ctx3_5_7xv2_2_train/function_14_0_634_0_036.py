def is_spam(message):
    import re

    # Check for spam keywords
    spam_keywords = ['신규방', '축하합니다', '▼클릭', '▲']

    for keyword in spam_keywords:
        if keyword in message:
            return True

    # Check for URLs
    url_pattern = re.compile(r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\\\'\\,]|(?:%[0-9a-fA-F][0-9a-fA-F]))+')
    urls = re.findall(url_pattern, message)

    if len(urls) > 0:
        return True

    return False