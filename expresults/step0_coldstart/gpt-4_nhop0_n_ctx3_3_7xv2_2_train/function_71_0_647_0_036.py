
import re

def is_spam(message):
    message = message.lower()

    # Detect and count URLs
    urls = re.findall('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', message)

    # Look for keywords and patterns associated with spam messages
    if ("vip" in message) or (len(urls) > 0) or (re.search(r'\d{1,2}[%]\s*↑', message)):
        return True

    # If none of the spam patterns are found, return False (not spam)
    return False
