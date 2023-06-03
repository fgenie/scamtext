
import re

def is_spam(message:str) -> bool:
    # Check for multiple consecutive newline characters or overly long URLs
    if re.search(r'\n{2,}', message) or re.search(r'http[s]?://[^\s]{20,}', message):
        return True

    # Check for an excessively high number of numeric characters or capital letters
    if re.search(r'[0-9]{5,}', message) or re.search(r'[A-Z]{4,}', message):
        return True

    # Check for Korean Won currency symbol
    if '원' in message:
        return True

    return False
