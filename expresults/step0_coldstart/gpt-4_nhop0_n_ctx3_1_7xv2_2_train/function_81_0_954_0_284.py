def is_spam(text: str) -> bool:
    import re

    # Check for typical spam keywords
    spam_keywords = [
        "광고",
        "판매",
        "수익",
        "인원 모집",
        "무료 거부",
    ]
    for keyword in spam_keywords:
        if keyword in text:
            return True

    # Check for excessive use of numbers, e.g., prices or profits
    numbers = re.findall(r"\d+", text)
    if len(numbers) > 5:
        return True

    # Check for multiple URLs
    urls = re.findall(r"https?://[\w\.-]+", text)
    if len(urls) > 1:
        return True

    # Check for excessive use of special characters, e.g., punctuation or symbols
    special_chars = re.findall(r"[\W_]+", text)
    if len(special_chars) > 5:
        return True

    return False