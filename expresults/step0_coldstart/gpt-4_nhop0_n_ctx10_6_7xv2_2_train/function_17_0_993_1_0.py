
import re

def is_spam(message):
    # Check for unusual URL shorteners
    url_shorteners_pattern = r"(bit\.ly|me2\.kr)"
    if re.search(url_shorteners_pattern, message):
        return True
    
    # Check for numbers followed by percentage signs or won signs
    numbers_pattern = r"[0-9]+(\s?)[\%원]"
    if re.search(numbers_pattern, message):
        return True
    
    # Check for unusual unicode characters
    unicode_characters_pattern = r"[\u2E80-\u33FF\uAC00-\uD7A3\U0001F600-\U0001F64F\U0001F680-\U0001F6FF]+"
    if re.search(unicode_characters_pattern, message):
        return True
    
    return False
