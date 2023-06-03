def is_spam(message):
    import re
    import string

    # Check for unusual characters
    unusual_characters = re.sub(r'[a-zA-Z0-9 \n\.]', '', message)
    unusual_characters_ratio = len(unusual_characters) / len(message)
    if unusual_characters_ratio > 0.05:
        return True

    # Check for repetitive content
    repetitions = re.findall(r'(\S+)(?:(?=\s+\1))+', message)
    if len(repetitions) > 0:
        return True

    # Check for excessive use of digits or short url
    digits_count = sum([1 for char in message if char.isnumeric()])
    digits_ratio = digits_count / len(message)
    if digits_ratio > 0.15:
        return True

    short_url_pattern = re.compile(r'https?:\/\/(me2\.kr|bit\.ly|t\.co)\/\S{0,15}')
    if len(short_url_pattern.findall(message)) > 0:
        return True

    return False