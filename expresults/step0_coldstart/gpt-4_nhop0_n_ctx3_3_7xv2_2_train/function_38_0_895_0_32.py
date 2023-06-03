def is_spam(message: str) -> bool:
    import re

    # Check for common spam indicators
    spam_indicators = [
        r"(?i)https?:\/\/",  # URLs
        r"(?i)ab?s?t?ly\/",  # Shortened URLs
        r"(?i)[A-Z]{2,}\d+",  # Uppercase letters followed by numbers
        r"(?i)KEY:\d+",      # 'KEY:' followed by numbers
        r"(?i)\d{1,2}[%％]",  # Percentage character
        r"(?i)[↑↗▽▼△▲]",     # Special characters
    ]

    for pattern in spam_indicators:
        if re.search(pattern, message):
            return True

    # Check if message has an unusually high ratio of special characters or numbers to letters
    special_chars = re.compile(r'[^a-zA-Z가-힣]')
    letters = re.compile(r'[a-zA-Z가-힣]')
    special_count = len(special_chars.findall(message))
    letter_count = len(letters.findall(message))

    if letter_count > 0:
        ratio = float(special_count) / float(letter_count)
        if ratio >= 0.5:
            return True

    return False