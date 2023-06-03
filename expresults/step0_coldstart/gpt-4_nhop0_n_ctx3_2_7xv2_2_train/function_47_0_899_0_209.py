
import re

def is_spam(message):
    # Check for urls
    url_pattern = re.compile(r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\\(\\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+')
    if url_pattern.findall(message):
        return True

    # Check for excessive use of numbers and special characters
    special_chars_pattern = re.compile(r'[^\w\s]')
    numbers_pattern = re.compile(r'\d{4,}')
    special_chars_count = len(special_chars_pattern.findall(message))
    numbers_count = len(numbers_pattern.findall(message))
    if special_chars_count > 2 or numbers_count > 0:
        return True

    # Check for words related to spam
    spam_words = ['상한가', '수익', '비밀번호', '단독제휴협약']
    if any(word in message for word in spam_words):
        return True

    # If none of the conditions above are met, it's likely not spam
    return False

