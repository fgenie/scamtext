def is_spam(message:str) -> bool:
    import re

    # Check for multiple consecutive special characters
    if re.search(r'\W{3,}', message):
        return True

    # Check for excessive capital letters
    if sum([1 for c in message if c.isupper()]) > len(message) // 3:
        return True

    # Check for URL-like patterns
    if re.search(r'(http(s)?://|www)[^\s]*', message):
        return True

    # Check for phone number-like patterns
    if re.search(r'\b(?:\+?[-.\s\(\)]*\d[-.\s\(\)]*){3,}\b', message):
        return True

    # Check for multiple line breaks
    if sum([1 for c in message if c == '\n']) > len(message) // 30:
        return True

    # If none of the above checks are true, consider the message normal.
    return False