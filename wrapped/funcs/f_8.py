
import re

def is_spam(message):
    # Check for ad-related keywords
    ad_keywords = ['(광고)', '무료거부', '주식', 'http', '추천']
    for keyword in ad_keywords:
        if keyword in message:
            return True

    # Check for excessive use of special characters
    special_chars = ['!', '?', '@', '#', '*', '=', '+']
    count = sum([message.count(char) for char in special_chars])
    if count >= 5:
        return True

    # Check for consecutive capital letters
    capital_letters = re.findall(r'[A-Z|가-힣]{3,}', message)
    if len(capital_letters) >= 2:
        return True

    # Check for numeric sequences
    numeric_sequences = re.findall(r'\d{3,}', message)
    if len(numeric_sequences) >= 1:
        return True

    # If none of the above conditions are met, consider the message as normal
    return False
