def is_spam(text: str) -> bool:
    import re

    # Rule 1: Check for special characters and digits repetition
    special_chars = re.compile(r"[●●*%<>▲▼]+")
    digits = re.compile(r"\d{2,}")
    if special_chars.search(text) and digits.search(text):
        return True

    # Rule 2: Check for domains with shortened urls
    urls = re.compile(r"(https?://)?\w{,5}\.\w{,3}/\w{,5}")
    if urls.search(text):
        return True

    # Rule 3: Check for excessive usage of upper case characters
    uppercase_ratio = sum(1 for c in text if c.isupper()) / len(text)
    if uppercase_ratio > 0.5:
        return True

    # Rule 4: Check for excessive usage of emoticons or heart symbols
    emoticons = re.compile(r"[♥]+")
    if emoticons.search(text) and len(emoticons.findall(text)[0]) >= 2:
        return True

    return False