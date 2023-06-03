
import re

def is_spam(message):
    # Check for URLs
    url_pattern = re.compile(r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\\(\\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+')
    if url_pattern.search(message):
        return True
        
    # Check for Korean characters
    korean_pattern = re.compile(r'[\u1100-\u11f9]|[\u3130-\u318f]|[\uac00-\ud7af]')
    if korean_pattern.search(message):
        return True
        
    # Check for encode numbers and special characters
    encoding_pattern = re.compile(r'[\d+][a-zA-Z]')
    if encoding_pattern.search(message):
        return True
        
    # Check for the presence of ads or advertisement in the message
    ad_pattern = re.compile(r'\b(ads?|광고)\b', flags=re.IGNORECASE)
    if ad_pattern.search(message):
        return True
    
    return False
