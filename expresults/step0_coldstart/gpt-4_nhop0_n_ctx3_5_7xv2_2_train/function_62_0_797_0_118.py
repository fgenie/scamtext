
import re

def is_spam(message: str) -> bool:
    # Check for (광고) or other advertisement keywords
    if '(광고)' in message or '추천' in message or '고객님' in message or '성과' in message:
        return True

    # Check for URLs
    url_pattern = re.compile(r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\\(\\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+')
    if url_pattern.search(message):
        return True

    # Check for phone numbers
    phone_pattern = re.compile(r'\d{2,4}-\d{3,4}-\d{4}')
    if phone_pattern.search(message):
        return True
    
    # Check for high number of special characters
    special_chars = set('!@#$%^&*()_+-=[]{}|;\':"<>?,./`~')
    message_chars = set(message)
    if len(message_chars.intersection(special_chars)) > 5:
        return True

    # Check for repetitions of certain patterns (e.g. 숫자 or 글자)
    number_pattern = re.compile(r'\d{5,}')
    letter_pattern = re.compile(r'(.)\1{3,}')
    if number_pattern.search(message) or letter_pattern.search(message):
        return True

    # If none of the previous conditions are met, the message is considered normal
    return False
