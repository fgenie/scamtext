def is_spam(text: str) -> bool:
    import re

    # Check for multiple consecutive capital letters
    capitals = re.findall(r'[A-Z]{3,}', text)
    if len(capitals) > 0:
        return True

    # Check for suspicious phrases
    spam_phrases = ['수익', '상한가', '공유', '바로가기', '적금출시', '즉시가입', '우대이자']
    for phrase in spam_phrases:
        if phrase in text:
            return True

    # Check for numerous consecutive special characters
    special_chars = re.findall(r'[\W_]{2,}', text)
    if len(special_chars) > 4:
        return True

    # Check for long URLs
    urls = re.findall(r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', text)
    if len(urls) > 0:
        for url in urls:
            if len(url) > 20:
                return True

    return False