def is_spam(message):
    import re

    # Spam keywords
    spam_keywords = ["체험반", "정확한 분석", "검증된 수익률", "종목상담", "추천주"]

    # URL pattern
    url_pattern = r"http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+"

    # Check for spam keywords in message
    for keyword in spam_keywords:
        if keyword in message:
            return True

    # Check for URL in message
    url_found = re.search(url_pattern, message)
    if url_found:
        # Check for excessive usage of special characters
        special_chars = "!@#$%^&*()-_+=[]{}|\\;:'\",.<>/?`~"
        special_char_count = sum(message.count(char) for char in special_chars)
        if special_char_count / len(message) > 0.1:  # Threshold of 10% special characters
            return True

    # Default to not spam
    return False