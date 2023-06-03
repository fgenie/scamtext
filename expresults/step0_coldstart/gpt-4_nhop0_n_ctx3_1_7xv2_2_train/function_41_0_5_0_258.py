def is_spam(message):
    import re

    # Check if the message contains special characters, numbers, and uppercase letters
    special_chars = re.findall(r'[\W]', message)
    numbers = re.findall(r'\d', message)
    uppercase_letters = re.findall(r'[A-Z]', message)
    urls = re.findall(r'(https?://[^\s]+)', message)

    # Calculate the ratio of special characters, numbers, and uppercase letters to the total length of the message
    special_char_ratio = len(special_chars) / len(message)
    number_ratio = len(numbers) / len(message)
    uppercase_ratio = len(uppercase_letters) / len(message)
    url_ratio = len(urls) / len(message)

    # Set thresholds to determine if a message is spam or not
    special_char_threshold = 0.3
    number_threshold = 0.2
    uppercase_threshold = 0.4
    url_threshold = 0.1

    if (special_char_ratio > special_char_threshold or
        number_ratio > number_threshold or
        uppercase_ratio > uppercase_threshold or
        url_ratio > url_threshold):
        return True
    else:
        return False