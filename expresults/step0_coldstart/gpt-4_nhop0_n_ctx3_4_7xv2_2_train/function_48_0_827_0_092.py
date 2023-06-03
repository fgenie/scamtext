def is_spam(message: str) -> bool:
    import re
    
    # Check for presence of URLs
    url_pattern = re.compile(r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\\(\\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+')
    has_url = bool(url_pattern.search(message))

    # Check for unusual symbols and text patterns
    unusual_symbols = re.compile(r'[▲▼↑※★▶▷ㆍ]+')
    has_unusual_symbols = bool(unusual_symbols.search(message))

    # Check for excessive use of special characters
    special_chars = re.compile(r'[!@#$%^&*(),.?":{}|<>]+')
    special_chars_count = len(special_chars.findall(message))

    # Check for presence of multiple consecutive numbers or percentage symbols
    numbers_percentage = re.compile(r'\d+%?')
    has_numbers_percentage = len(numbers_percentage.findall(message)) > 2

    # Check for excessive use of capital letters
    capital_letters = len(re.findall(r'[A-Z]', message))
    total_characters = len(message)
    capital_ratio = capital_letters / total_characters if total_characters > 0 else 0

    # Determine if the message is spam based on the combined conditions
    return has_url or has_unusual_symbols or special_chars_count > 5 or has_numbers_percentage or capital_ratio > 0.5