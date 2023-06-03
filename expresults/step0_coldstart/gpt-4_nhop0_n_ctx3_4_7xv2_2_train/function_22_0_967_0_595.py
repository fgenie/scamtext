
import re

def is_spam(message: str) -> bool:
    # Check for URL shorteners
    url_shorteners = r"(bit\.ly|me2\.kr|openkakao\.at)"
    if re.search(url_shorteners, message):
        return True
    
    # Check for unnecessary special characters (., /, +, etc.) between words
    special_chars = r"(\w[.,/+]+\w)"
    if re.search(special_chars, message):
        return True
    
    # Check for capitalization
    count_upper = sum(1 for c in message if c.isupper())
    count_words = len(message.split())
    if count_upper / count_words > 0.5:
        return True
    
    # Check for repeated messages, like "◆ openkakao.at/qwscvzx ◆"
    repeated_messages = r"(\S+\s+){2,}"
    if re.search(repeated_messages, message):
        return True
    
    return False
