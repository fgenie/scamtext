
import re

def is_spam(text):
    # List of regular expressions for spam patterns
    spam_patterns = [
        ".*\d{6}.*",
        ".*http.*",
        ".*VIP.*",
        ".*클릭.*",
        ".*종료.*",
        ".*이번에는.*",
        ".*이사비지원.*",
        ".*EE84.*",
        ".*손절.*",
        "^4월\d+일.*",
    ]
    # Check if the text matches any of the spam patterns
    for pattern in spam_patterns:
        if re.match(pattern, text):
            return True
    
    # If the text does not match any of the spam patterns, it is considered normal
    return False
