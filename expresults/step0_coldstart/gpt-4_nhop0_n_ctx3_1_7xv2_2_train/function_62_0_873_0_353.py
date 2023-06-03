
import re

def is_spam(text):
    # Check if the message includes a link with 'me2.kr' which is predominantly found in spam messages
    if 'https://me2.kr' in text:
        return True
    
    # Check for special characters like '!?*' that are more likely to be found in spam messages
    if re.search(r'[!?*]', text):
        return True
    
    # Check for non-space capital letters followed by lowercase letters (e.g., AI사업본, B기업, VIP체험반)
    if re.search('(?<=\\s)[A-Z][a-z]+', text):
        return True
    
    # Check for dates (e.g., 17日) or numbers followed by special characters (e.g., 4월)
    if re.search(r'\d+(\W|$)', text):
        return True
    
    return False
