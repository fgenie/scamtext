
import re

def is_spam(message):
    # Check for presence of links
    urls = re.findall(r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\\(\\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', message)
    if len(urls) > 0:
        return True

    # Check for presence of special characters and numbers
    content_check = re.findall(r'[0-9!@#\\\%^&*(),.?":{}|<>]', message)
    if len(content_check) >= len(message) / 2:
        return True

    # Check for non-Korean characters
    non_korean = re.findall(r'[^가-힣ㄱ-ㅎa-zA-Z\s]', message)
    if len(non_korean) > 0:
        return True

    return False
