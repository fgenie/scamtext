def is_spam(message):
    import re

    # Check for suspicious keywords
    spam_keywords = ["지니틱스", "나노 수익", "체험반", "악성광고", "텔레그램", "적중"]
    for keyword in spam_keywords:
        if keyword in message:
            return True

    # Check for existence of URLs
    url_pattern = re.compile(r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\\(\\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+')
    urls = re.findall(url_pattern, message)
    if len(urls) > 0:
        return True

    return False