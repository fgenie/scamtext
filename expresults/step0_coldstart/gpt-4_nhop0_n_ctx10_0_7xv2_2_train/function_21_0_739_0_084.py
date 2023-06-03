def is_spam(message: str) -> bool:
    import re

    # Check for common spam phrases and patterns
    spam_phrases = [
        "목표달성",
        "특별찬스잡으세요",
        "종목적중",
        "※",
        "ⓖ",
        r"http[s]?://(?:[a-zA-Z]|[0-9]|[-@._:/])+",
    ]

    # Check for excessive use of special characters and numbers
    special_chars = r"[!@#$%^&*(),.?\":{}|<>]"
    excessive_special_chars = re.findall(special_chars, message)
    numbers_in_message = re.findall(r"\d+", message)

    # Classify as spam if any spam phrase is found or if special characters & numbers occur too frequently
    if any(re.search(pattern, message) for pattern in spam_phrases):
        return True
    elif len(excessive_special_chars) > 5 or len(numbers_in_message) > 5:
        return True
    else:
        return False