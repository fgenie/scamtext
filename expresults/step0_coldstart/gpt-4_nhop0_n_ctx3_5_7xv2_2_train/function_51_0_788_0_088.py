
import re

def is_spam(message):
    # Check for suspicious URL patterns
    suspicious_urls = ["me2.kr", "han.gl"]
    for url in suspicious_urls:
        if url in message:
            return True

    # Check for non-standard characters
    non_standard_chars = re.findall("[^a-zA-Z0-9가-힣\s\.,!?]", message)
    if len(non_standard_chars) > 5:  # Arbitrary threshold
        return True

    # Check for excessive numeric values
    numbers = re.findall("\d+", message)
    if len(numbers) > 3:  # Arbitrary threshold
        return True

    return False
