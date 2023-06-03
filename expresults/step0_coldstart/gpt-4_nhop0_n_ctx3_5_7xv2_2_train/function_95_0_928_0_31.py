
import re

def is_spam(message):
    # Check for presence of URL
    url_pattern = re.compile(r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\\(\\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+')
    result = re.search(url_pattern, message)
    if result:
        return True
    
    # Check for unusual characters
    unusual_pattern = re.compile(r'[^가-힣a-zA-Z0-9\s.,?!]+')
    result = re.search(unusual_pattern, message)
    if result:
        return True

    # Check for repeated characters
    repeated_pattern = re.compile(r'(.)\1{2,}')
    result = re.search(repeated_pattern, message)
    if result:
        return True
    
    return False
