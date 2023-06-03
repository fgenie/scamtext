
import re
import string

def is_spam(message):
    # Check for link patterns
    link_pattern = r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\\(\\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+'
    if re.search(link_pattern, message):
        return True

    # Check for special characters or symbols
    special_chars = string.punctuation.replace("_", "") # "_" is allowed
    if any(char in special_chars for char in message):
        return True
    
    # Check for suspicious words
    suspicious_words = ["신규", "카>에볼", "노>신규", "지>신규감사쿠폰"]
    for word in suspicious_words:
        if word in message:
            return True
            
    return False
