
import re

def is_spam(message):
    # Spam keywords
    spam_keywords = ['광고', '지원', '미공개', '알려드리', '지금', '안전', '최대']
    
    # Check for spam keywords in the message
    for keyword in spam_keywords:
        if keyword in message:
            return True
    
    # Check for excessive capitalization
    if len([c for c in message if c.isupper()]) > len(message) * 0.5:
        return True

    # Check for URLs
    if re.search(r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\\(\\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', message):
        return True

    # Check for specific patterns often found in spam messages, such as sequences of 4 or more digits
    if re.search(r'\d{4,}', message):
        return True

    # If the message doesn't match any of the above conditions, it's considered a normal message
    return False
