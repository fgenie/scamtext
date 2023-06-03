def is_spam(message):
    import re
    
    # Check for presence of URLs
    url_pattern = re.compile(r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+')
    has_url = bool(url_pattern.search(message))
    
    # Check for excessive use of special characters
    special_chars_pattern = re.compile(r'[!@#$%^&*(),.?":{}|<>]')
    special_chars = special_chars_pattern.findall(message)
    is_excessive_special_chars = len(special_chars) * 2 >= len(message)
    
    # Check for presence of numbers
    number_pattern = re.compile(r'\d+')
    has_numbers = bool(number_pattern.search(message))
    
    # Check for presence of non-alphabetic characters (e.g. Korean text)
    non_alphabetic_pattern = re.compile(r'[^a-zA-Z\s]')
    non_alphabetic_chars = non_alphabetic_pattern.findall(message)
    contains_non_alphabetic = len(non_alphabetic_chars) > len(message) // 2
    
    # If the message contains URLs, excessive use of special characters, has numbers, or contains non-alphabetic characters,
    # classify it as spam
    return has_url or is_excessive_special_chars or has_numbers or contains_non_alphabetic