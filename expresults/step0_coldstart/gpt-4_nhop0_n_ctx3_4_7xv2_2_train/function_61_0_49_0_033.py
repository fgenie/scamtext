def is_spam(message: str) -> bool:
    import re

    # Check for excessive special characters and digits
    special_characters = re.findall(r'[!@#$%^&*()-=_+{}\[\];\'\":,.<>?]', message)
    digits = re.findall(r'\d', message)
    if len(special_characters) > len(message) * 0.3 or len(digits) > len(message) * 0.3:
        return True

    # Check for short URLs
    url_regex = r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\\(\\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+'
    short_url_regex = r'(http[s]?:\/\/me2\.kr\/\S{3})(?:\s|$)'
    urls = re.findall(url_regex, message)
    short_urls = re.findall(short_url_regex, message)
    if len(urls) > 0 and len(short_urls) == len(urls):
        return True

    return False