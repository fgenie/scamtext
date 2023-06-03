
import re

def is_spam(message):
    # Check if the message has too many special characters
    special_chars = re.findall(r'[^\w\s]', message)
    if len(special_chars) / len(message) > 0.2:
        return True

    # Check if the message contains a URL
    url_regex = r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\\|\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+'
    if re.search(url_regex, message):
        return True

    # Check if the message contains repeated phrases
    tokens = message.split()
    if len(set(tokens)) / len(tokens) < 0.5:
        return True

    # Check if the message contains a percentage followed by an upward sign
    if re.search('\d+% ?(상승|증가)', message):
        return True

    return False
