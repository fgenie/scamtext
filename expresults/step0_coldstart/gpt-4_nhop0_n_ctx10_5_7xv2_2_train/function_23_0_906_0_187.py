
import re

def is_spam(text):
    # Check for message starting with '*' or containing '*text*' format
    if text.startswith('*') or "*" in text:
        return True
    
    # Check for multiple consecutive exclamation marks, question marks or both
    if re.search(r'[!?,]{2,}', text):
        return True
    
    # Check for excessive usage of special characters or digits
    if re.search(r'[0-9_%\$@#⊃[\]^><`]', text):
        return True
    
    # Check for presence of suspicious links or shortened URLs
    suspecious_links = ['me2.kr', 'buly.kr', 'tuney.kr', 'vvd.bz']
    for link in suspecious_links:
        if link in text:
            return True

    return False
