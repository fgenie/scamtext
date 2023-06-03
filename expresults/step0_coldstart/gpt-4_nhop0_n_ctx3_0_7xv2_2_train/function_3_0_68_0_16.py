def is_spam(message):
    import re
    
    # Define potential spam characteristics
    short_link_pattern = re.compile(r'bit\.ly|me2\.kr', re.IGNORECASE)
    percentage_pattern = re.compile(r'\d{1,3}%')
    stock_code_pattern = re.compile(r'\([0-9]{6}\)')
    random_chars_pattern = re.compile(r'[ㄱ-ㅣ]+')

    # Check message for spam characteristics
    if short_link_pattern.search(message):
        return True
    if percentage_pattern.search(message):
        return True
    if stock_code_pattern.search(message):
        return True
    if random_chars_pattern.search(message):
        return True

    # If none of the characteristics are found, return False
    return False