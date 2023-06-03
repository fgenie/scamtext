
import re

def is_spam(message: str) -> bool:
    # Check for special characters
    if re.search(r'[!%^*())><&$#]+', message):
        return True

    # Check for links
    if re.search(r'(https?://\S+)', message):
        return True

    # Check for unusual repetition of capital letters
    if len(re.findall(r'[A-Z]{2,}', message)) > 1:
        return True

    # Check for percentage
    if re.search(r'\d+%+', message):
        return True

    return False

