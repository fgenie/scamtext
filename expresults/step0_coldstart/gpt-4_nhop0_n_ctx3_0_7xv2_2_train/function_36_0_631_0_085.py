def is_spam(message):
    import re
    
    # Check for URL presence
    url_pattern = re.compile(r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\\(\\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+')
    has_url = bool(url_pattern.search(message))

    # Check for excessive capitalization
    uppercase_count = sum(1 for c in message if c.isupper())
    uppercase_ratio = uppercase_count / len(message)
    
    # Check for symbols and alphanumeric characters
    symbol_pattern = re.compile(r'[@_!#$%^&*()<>?/\\\\|}{~:]')
    has_symbols = bool(symbol_pattern.search(message))

    non_alphanumeric_count = sum(1 for c in message if not c.isalnum() and not c.isspace())
    non_alphanumeric_ratio = non_alphanumeric_count / len(message)
    
    if (has_url and has_symbols) or uppercase_ratio > 0.3 or non_alphanumeric_ratio > 0.2:
        return True
    else:
        return False