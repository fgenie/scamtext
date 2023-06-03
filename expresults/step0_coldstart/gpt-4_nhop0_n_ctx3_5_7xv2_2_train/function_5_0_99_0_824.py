
import re

def is_spam(message: str) -> bool:
    # Check for URL shorteners
    url_shorteners = ["me2.kr"]
    for url_shortener in url_shorteners:
        if url_shortener in message:
            return True

    # Check for non-ASCII characters
    non_ascii_chars = re.findall(r'[\u0080-\uFFFF]', message)
    if len(non_ascii_chars) > 2:
        return True

    # Check for high ratio of special characters
    special_chars = re.findall(r'[!@#$%^&*()+=\[\]{}|;,<>/?]+', message)
    if len(special_chars) / len(message) > 0.1:
        return True

    # Check for use of specific phrases
    spam_phrases = ["체험반"]
    for phrase in spam_phrases:
        if phrase in message:
            return True

    return False
