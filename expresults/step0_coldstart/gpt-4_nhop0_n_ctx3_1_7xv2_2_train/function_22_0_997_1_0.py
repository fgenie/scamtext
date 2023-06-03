
import re

def is_spam(text: str) -> bool:
    # Check for ads or suspicious links
    if re.search('(광고)|me2\.kr', text):
        return True

    # Check for suspicious unicode characters
    if re.search('[^\x00-\x7F]', text):
        return True
        
    # Check for excessive punctuation
    if re.search(r'([!?.]){2,}', text):
        return True

    # Check for unusual capitalization
    if re.search(r'([A-Z]|[가-힣]){4,}', text):
        return True

    return False
