
import re

def is_spam(message):
    # Rules for detecting spam
    spam_rules = [
        r"https?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+", # Check for presence of URLs
        r"[월 천 고정수입!]", # Check for specific spam keyword combinations
        r"kakaotalk\.it", # Check for specific suspicious URL patterns
        r".*\d{2}\s*[%]↑.*", # Check for keyword with percentage increase
    ]
    
    # Apply spam rules to the message
    for rule in spam_rules:
        if re.search(rule, message):
            return True
    return False
