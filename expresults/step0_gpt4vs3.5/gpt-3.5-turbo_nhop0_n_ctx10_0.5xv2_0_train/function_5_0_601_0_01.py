
import re

def is_spam(message):
    # regex pattern to match URLs starting with "http://", "https://", or "www."
    url_pattern = re.compile(r"https?://|www\.", re.IGNORECASE)
    
    # regex pattern to match strings consisting of only digits and/or hyphens
    number_pattern = re.compile(r"^[0-9-]+$")
    
    if url_pattern.search(message):
        # if the message contains a URL, it is likely to be spam
        return True
    elif number_pattern.search(message):
        # if the message consists only of digits and/or hyphens, it is likely to be spam
        return True
    else:
        # if none of the above conditions are met, the message is classified as normal
        return False
