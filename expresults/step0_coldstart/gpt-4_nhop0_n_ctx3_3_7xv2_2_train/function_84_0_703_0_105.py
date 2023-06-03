
import re

def is_spam(message: str) -> bool:
    # Check for presence of http or https links
    if re.search(r'http[s]?://\S+', message):
        return True

    # Check for excessive usage of special characters like . , + and %
    special_chars = sum([1 for char in message if char in '.+,%'])
    if special_chars / len(message) > 0.1:
        return True

    # Check for presence of marketing related words
    marketing_words = ['(광고)', '선물매매', '1:1교육', '무료거부']
    for word in marketing_words:
        if word in message:
            return True
            
    return False
