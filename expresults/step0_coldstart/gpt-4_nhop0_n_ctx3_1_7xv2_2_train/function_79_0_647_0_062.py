def is_spam(message: str) -> bool:
    import re

    # Check for excessive capitalization
    uppercase_ratio = sum(1 for char in message if char.isupper()) / len(message)
    if uppercase_ratio > 0.5:
        return True

    # Check for numbers followed by % sign
    if re.search(r'\d+%\s*↑', message):
        return True

    # Check for presence of URLs or shortened URLs
    if re.search(r'(https?:\/\/\S+)|me2\.kr\/\S+', message):
        return True

    # Check for excessive use of special characters
    special_chars_ratio = sum(1 for char in message if char in '!@#$%^&*()') / len(message)
    if special_chars_ratio > 0.1:
        return True

    return False