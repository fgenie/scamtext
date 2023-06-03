
import re

def is_spam(message):
    # Define spammy patterns to look for
    spam_patterns = [
        r'https?:\/\/\S+', # URLs
        r'[A-Za-z0-9]+@[a-z]+\.[a-z]+', # E-mail addresses
        r'\bvip\b', # Words like 'vip'
        r'\b\d{5,}\b', # Numbers with 5 or more digits
        r'\b\W{5,}\b', # 5 or more special characters consecutively
        r'\b([A-Z]{3,}[a-z]*)|([a-z]*[A-Z]{3,})\b' # 3 or more consecutive capital letters in a word
    ]

    # Check if any of the spam patterns are present in the message
    for pattern in spam_patterns:
        if re.search(pattern, message, re.IGNORECASE):
            return True

    # If none of the patterns are present, consider it a normal message
    return False
