
import re

def is_spam(message):
    # Check if message contains URL
    url_pattern = re.compile(r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+')
    
    if url_pattern.search(message):
        # Check for number usage pattern frequently found in spam messages
        number_pattern = re.compile(r'\d\d[日]')
        
        if number_pattern.search(message):
            return True
        else:
            return False
            
    return False

