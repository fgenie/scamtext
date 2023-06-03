def is_spam(text: str) -> bool:
    import re

    # Patterns to identify spam
    spam_patterns = [
        r"[\s\S]*[ㅗㅑㅓ]+[ㅡㅑ]+[\s\S]*",
        r"[\s\S]*(?=https:\/\/me2\.kr)[\s\S]*"
    ]

    # Check if any spam pattern matches the text
    for pattern in spam_patterns:
        if re.match(pattern, text):
            return True

    return False