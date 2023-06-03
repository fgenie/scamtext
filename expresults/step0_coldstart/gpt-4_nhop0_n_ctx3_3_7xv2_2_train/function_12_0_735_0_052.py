
import re

def is_spam(message):
    # Checking for presence of URLs
    url_pattern = r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+'
    if re.search(url_pattern, message):
        return True

    # Checking for presence of kakaotalk links
    if "kakaotalk.it/" in message:
        return True

    # Check for sudden percentage values
    percentage_pattern = r'\d{1,3}%'
    if re.search(percentage_pattern, message):
        return True

    # If none of the above conditions are met, the message is considered normal
    return False
