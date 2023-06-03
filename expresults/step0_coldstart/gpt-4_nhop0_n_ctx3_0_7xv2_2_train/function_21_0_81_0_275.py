
import re

def is_spam(message):
    # Check for common spam keywords in the message
    spam_keywords = ["(광고)", "https://", "www.", "입장코드", "무료거부", "이벤트", "추가Event", "신규", "어렵운시기에"]
    
    # Check for excessive use of special characters and capitalization
    special_characters = re.findall(r'[\W\s]', message)
    capital_characters = re.findall(r'[A-Z]', message)

    # Calculate the ratios of special characters and capital characters to the length of the message
    special_chars_ratio = len(special_characters) / len(message)
    capital_chars_ratio = len(capital_characters) / len(message)

    # If any of the spam keywords is in the message, or if the ratio of special characters is too high, consider the message as spam
    if any(keyword in message for keyword in spam_keywords) or special_chars_ratio > 0.3 or capital_chars_ratio > 0.3:
        return True
    else:
        return False
