
import re

def is_spam(message: str) -> bool:
    # Check for common spam characteristics
    url_regex = r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\\(\\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+'
    money_regex = r'[\d,]+원'
    percent_regex = r'\d+%'

    # Check if message contains URL
    if re.search(url_regex, message):
        return True

    # Check if message contains money or percentage expressions
    if re.search(money_regex, message) or re.search(percent_regex, message):
        return True

    # Check for suspicious leading/trailing whitespace
    if message.strip() != message:
        return True

    # If none of the above checks have been met, consider the message as normal (non-spam)
    return False
