def is_spam(message):
    import re

    # Check for typical spam phrases and symbols
    spam_phrases = ["상한가", "특별 할인", "무료수신거부", "%", "MOU", "특가", "소문난 주식"]

    for phrase in spam_phrases:
        if phrase in message:
            return True

    # Check for excessive use of special characters
    special_chars = re.findall(r"[!@#$%^&*()\-_=+[\]{};:\'\"|,<.>/?]+", message)
    if len(special_chars) > 5:
        return True

    # Check for suspicious URLs
    urls = re.findall(r"http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\\(\\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+", message)
    if len(urls) > 1:
        return True

    # Check for excessive use of numbers
    numbers = re.findall(r"[0-9]+", message)
    if len(numbers) > 3:
        return True

    # Check for non-Korean characters
    non_korean = re.findall(r"[^ㄱ-하-ㅣ가-힣\s]+", message)
    if len(non_korean) > 5:
        return True

    return False