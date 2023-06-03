
import re

def is_spam(message):
    # Check for spam keywords
    keywords = ["광고", "투자", "MOU", "체험반", "bit.ly", "me2.kr"]
    for keyword in keywords:
        if keyword in message:
            return True
    
    # Check for phone number format
    phone_pattern = re.compile(r'\d{2,4}[-\s]?(\d{3,4}[-\s]?)\d{4}')
    if phone_pattern.search(message):
        return True

    # Check for excessive use of special characters
    special_characters = "!@#$%^&*()_+={}[]|\\:;'\"<>?,./"
    count = sum(1 for char in message if char in special_characters)
    if count / len(message) > 0.25:
        return True

    return False
