
import re

def is_spam(message):
    # Check for large capital letter usage
    capitals_ratio = sum(1 for char in message if char.isupper()) / len(message)
    if capitals_ratio > 0.5:
        return True

    # Check for URL-shortening services
    if re.search(r'(https?|ftp)://me2\.kr|openkakao\.at', message):
        return True
        
    # Check for mentioned keywords that are commonly associated with spam messages
    keywords = ['적중', '최고급', '선취매', '수급주', '광고', '할인', '대출', '금전']
    for keyword in keywords:
        if keyword in message:
            return True

    # Check for excessive special characters
    special_chars = sum(1 for char in message if not char.isalnum())
    if special_chars > 3:
        return True
        
    return False 
