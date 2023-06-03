def is_spam(message):
    import re

    # Check for URL patterns
    url_pattern = re.compile(r'(http(s)?://|www\.)(\w+\.)+\w+|[a-zA-Z]+[0-9]+.(\w+/)+\w+/(\w+.*)+')
    if url_pattern.search(message):
        return True

    # Check for excessive use of special characters
    special_chars_pattern = re.compile(r'[!"#$%&\'*+,-./:;<=>?@[\]^_`{|}~]')
    special_chars_count = len(special_chars_pattern.findall(message))
    if special_chars_count >= 5:
        return True

    # Check for excessive use of numbers
    numbers_pattern = re.compile(r'\d')
    numbers_count = len(numbers_pattern.findall(message))
    if numbers_count >= 5:
        return True

    return False