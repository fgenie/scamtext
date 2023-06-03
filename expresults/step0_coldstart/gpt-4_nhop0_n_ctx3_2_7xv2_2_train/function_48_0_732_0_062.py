def is_spam(message: str) -> bool:
    import re

    # Check for common spam words or phrases in the message
    spam_words = [
        "광고",
        "무료거부",
        "목표달성",
        "http",
        "입장번호",
        "상승",
        "수익실현"
    ]
    for word in spam_words:
        if word in message:
            return True

    # Check for suspicious patterns
    urls = re.findall(r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\\(\\)\\,]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', message)
    if len(urls) > 1:  # If the message has more than one URL, it might be spam
        return True

    # Check if the message has long strings of the same character (e.g. "------")
    if re.search(r"(.)\1{4,}", message):
        return True

    return False