def is_spam(message):
    import re

    # Define keywords and patterns that often appear in spam messages
    spam_keywords = ['광고', '무료수신거부', '대출', '%', '증정', '이벤트']
    spam_url_pattern = re.compile(r'(http|https)://[a-zA-Z0-9\./-_]+\.[a-zA-Z]{2,}')

    # Check if the message contains any spam keywords
    for keyword in spam_keywords:
        if keyword in message:
            return True

    # Check if the message contains any suspicious URLs
    if spam_url_pattern.search(message):
        return True

    # Otherwise, the message is not spam
    return False