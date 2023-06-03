def is_spam(message: str) -> bool:
    import re

    # Pattern for matching typical spam attributes
    spam_pattern = re.compile(
        r'((신입|올인|달성|ㅣ밥|울|톡)[\s\.\-]*(\d{1,3}\s*[%|원]))|'
        r'(주[0-9]+회취킨)|'
        r'(url\.kr)|(abit\.ly)|'
        r'(KEY:[\s]*\d{4})|'
        r'(([0-9]+)만원)'
    )

    # Check if the message matches spam pattern
    if spam_pattern.search(message):
        return True
    else:
        return False