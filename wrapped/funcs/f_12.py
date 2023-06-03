def is_spam(message):
    import re

    # Check if the message contains a URL with a suspicious domain
    suspicious_domains = ['han.gl', 'me2.kr', 'bit.ly', 'ko.gl', 'vo.la', 'asq.kr', 'buly.kr']
    url_pattern = r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\\(\\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+'
    urls = re.findall(url_pattern, message)
    for url in urls:
        for domain in suspicious_domains:
            if domain in url: 
                return True

    # Check if the message contains a high percentage of special characters like ()[]
    special_char_pattern = r'[!@#$%^&*_+=|;:?<>,.(){}\[\]]'
    special_chars = re.findall(special_char_pattern, message)
    if len(special_chars) / len(message) > 0.3:
        return True

    # Check if the message contains a high percentage of numerical characters
    numerical_char_pattern = r'[0-9]'
    numerical_chars = re.findall(numerical_char_pattern, message)
    if len(numerical_chars) / len(message) > 0.4:
        return True

    # Check if the message contains sequential repetitions of newline characters
    consecutive_newline_pattern = r'\s?(\n){2,}'
    consecutive_newlines = re.findall(consecutive_newline_pattern, message)
    if len(consecutive_newlines) > 0:
        return True

    # Check if there are too many capital letters
    capital_letters = re.findall(r'[A-Z]', message)
    if len(capital_letters) / len(message) > 0.2:
        return True

    return False