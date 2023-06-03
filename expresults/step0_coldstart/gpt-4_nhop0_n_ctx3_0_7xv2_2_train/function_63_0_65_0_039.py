def is_spam(message: str) -> bool:
    import re

    keywords = ["추천주", "체험", "실력입증", "보내기", "돌파", "한농화성", "VIP정보방", "증권사부장출신", "안정적인 수익"]

    # Check if the message contains any of the predefined spam keywords
    for keyword in keywords:
        if keyword in message:
            return True

    # Check if the message contains a URL
    url_pattern = re.compile(r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+')
    if re.search(url_pattern, message):
        return True

    # If none of the conditions match, it's not a spam message
    return False