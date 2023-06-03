
import re

def is_spam(message):
    # check for consecutive special characters
    consecutive_special_chars = re.compile(r'[^\w\s]{2,}')
    if consecutive_special_chars.search(message):
        return True
    
    # check for urls
    url = re.compile(r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*()\],]|(?:%[0-9a-fA-F][0-9a-fA-F]))+')
    if url.search(message):
        return True

    # check for marketing-related phrases
    marketing_phrases = ['체험반', '무료체험반']
    for phrase in marketing_phrases:
        if phrase in message:
            return True

    # if none of the above conditions is satisfied
    return False
