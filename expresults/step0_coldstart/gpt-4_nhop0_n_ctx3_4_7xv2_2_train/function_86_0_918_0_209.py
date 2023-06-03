
import re

def is_spam(message):
    # Look for multiple consecutive capital letters, numbers, or special characters
    pattern1 = re.compile(r'([A-Z0-9\W_]){3,}')
    
    # Look for URLs with suspicious domains (me2.kr, han.gl)
    pattern2 = re.compile(r'(https?:\/\/(me2\.kr|han\.gl)\/\S*)')

    # Check if either pattern is found in the message
    if pattern1.search(message) or pattern2.search(message):
        return True
    else:
        return False
