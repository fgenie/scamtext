
import re

def is_spam(message: str) -> bool:
    # Check for multiple exclamation marks or question marks
    if re.search(r'[!?]{2,}', message):
        return True

    # Check for URL shortening services
    url_shorteners = ['bit.ly', 'me2.kr', 'tinyurl.com', 'goo.gl', 'ow.ly', 't.co']
    for shortener in url_shorteners:
        if shortener in message:
            return True

    # Check for numbers that may indicate promotions or limited offers (e.g., discounts, limited slots)
    if re.search(r'\d{2,}', message):
        return True

    # Check for all-uppercase phrases, which may indicate aggressive marketing
    if re.search(r'\b[A-Z]{2,}\b', message):
        return True

    # If none of the above conditions is met, consider the message as a normal message
    return False
