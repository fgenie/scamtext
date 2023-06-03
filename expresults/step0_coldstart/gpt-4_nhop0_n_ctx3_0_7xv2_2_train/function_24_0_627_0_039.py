
import re

def is_spam(message):
    # Define spam patterns
    spam_patterns = [
        r'http[s]?:\/\/\S*',   # URLs
        r'[0-9]{1,2}[\.,만]{0,2}[0-9]{3,4}(선착순|종료)',  # Large numbers related to profit or positions
        r'[3-5]{1}[0-9]{1}대',   # Specific age groups
        r'\([^()]+\)\s+https?:\/\/\S+',  # URL enclosed in brackets
        r'\w+\|\d+[일]?추천',  # Some kind of recommendation
        r'\([^()]+\)의? 고객에', # Specific people as customers
        r'[0-9]+% 할인' # High discount percentages
    ]
    
    # Normalize message
    message = message.lower()

    # Check for spam patterns in the message
    for pattern in spam_patterns:
        if re.search(pattern, message):
            return True

    # If no spam pattern found, then it's not spam
    return False
