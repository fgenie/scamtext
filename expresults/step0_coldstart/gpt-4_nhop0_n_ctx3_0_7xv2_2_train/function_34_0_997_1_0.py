
import re

def is_spam(message):
    # Check for unusual unicode characters that are commonly used in spam messages
    if re.search(r'[\u1100-\u11FF\u3131-\u318E\uAC00-\uD7A3]', message):
        return True

    # Check for presence of URLs using regex pattern
    url_pattern = re.compile(r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+')
    if url_pattern.search(message):
        return True

    # Check for excessive use of numbers and special characters
    if len(re.findall(r'\d+', message)) > 3 or len(re.findall(r'[!@#$%^&*(),.?":{}|<>]', message)) > 5:
        return True

    return False
