
import re

def is_spam(message):
    # check for presence of URLs
    url_pattern = re.compile(r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\\(\\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+')
    if url_pattern.search(message):
        return True
    
    # check for excessive use of non-alphabetic characters
    non_alpha_pattern = re.compile(r'[^a-zA-Z가-힣\s]+')
    non_alpha_count = len(non_alpha_pattern.findall(message))
    if non_alpha_count > 4:
        return True

    # check for abnormal message length
    message_length = len(message)
    if message_length > 100:
        return True

    # if none of the above conditions are met, it's considered a normal message
    return False

