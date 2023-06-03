
import re

def is_spam(message):
    # Check for excessive punctuation or capitalization
    if re.search(r'[!?.]{2,}', message) or re.search(r'[A-Z]{4,}', message):
        return True

    # Check for presence of URLs
    if re.search(r'https?://\S+', message) or re.search(r'www\.\S+', message):
        return True

    # Check for suspicious patterns such as number sequences or repetition of characters
    if re.search(r'\d{4,}', message) or re.search(r'(.)\1{2,}', message):
        return True

    return False
