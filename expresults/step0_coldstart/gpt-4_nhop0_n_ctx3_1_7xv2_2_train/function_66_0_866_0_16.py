
import re

def is_spam(text: str) -> bool:
    # Check for unusual URL pattern
    url_pattern = re.compile(r'(https?://|www\.|me2\.kr)') 
    if url_pattern.search(text):
        return True
    
    # Check for excessive use of special characters
    special_chars = re.compile(r'[%/|％]')
    if len(special_chars.findall(text)) > 2:
        return True

    # Check for unusually big differences in letter casing
    lower_count = sum(c.islower() for c in text)
    upper_count = sum(c.isupper() for c in text)
    if lower_count > 10 * upper_count or upper_count > 10 * lower_count:
        return True

    # Check for specific spam keywords
    keywords = ['입', '출', '무/한', '증권', '콩']
    for keyword in keywords:
        if keyword in text:
            return True

    return False
