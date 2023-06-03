def is_spam(message: str) -> bool:
    import re

    # Check for multiple special characters in the message
    special_characters = re.findall(r'[^\w\s]', message)
    if len(special_characters) > 3:
        return True

    # Check for patterns that indicate spam messages
    spam_patterns = [
        r'https?://\w+\.\w+',  # URLs
        r'\d+%?↑',  # Percentage with or without upward arrow
        r'\w{2}[\/]?\w{2}',  # Code-like pattern (e.g. '코/드' or '코드')
        r'\(\w\d\)'  # Parentheses with a character and a digit (e.g. '(x4)')
    ]

    for pattern in spam_patterns:
        if re.search(pattern, message):
            return True

    return False