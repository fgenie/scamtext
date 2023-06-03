
import re

def is_spam(message):
    url_pattern = r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\\(\\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+'
    korean_pattern = r'\S*[^\x00-\x7F]+(?:\S)*'

    if re.search(url_pattern, message) and re.search(korean_pattern, message):
        splitted_text = message.split()
        if len(splitted_text) > 5:
            return True
        if any(word.isdigit() for word in splitted_text):
            return True

    return False
