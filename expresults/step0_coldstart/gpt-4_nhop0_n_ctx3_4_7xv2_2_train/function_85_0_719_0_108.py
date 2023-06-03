
import re

def is_spam(message: str) -> bool:
    # Spam characteristics
    url_pattern = r'https?://(?:[-\w.]|(?:%[\da-fA-F]{2}))+'
    spam_words = ["지급", "클릭", "체크", "목표가", "오후"]
    excessive_special_chars = r'[!@#$%^&*()-+=]{2,}'

    # Check for URL in the message
    if re.search(url_pattern, message):
        return True
    
    # Check for spam words in the message
    if any(spam_word in message for spam_word in spam_words):
        return True

    # Check for excessive use of special characters
    if re.search(excessive_special_chars, message):
        return True

    return False
