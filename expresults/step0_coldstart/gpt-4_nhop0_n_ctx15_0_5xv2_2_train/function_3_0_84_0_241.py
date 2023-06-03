
import re


def is_spam(text):
    # Regular expressions for common spam patterns
    spam_keywords = [r'(https?://\S+)', r'(광고)', r'(상한가)', r'(수익실현)', r'(무료거부)',
                     r'(카톡방)', r'(월체험반)', r'(추천주)', r'(선물)', r'(MOU체결)', r'(공시)']

    # Check for keyword pattern in message
    for keyword in spam_keywords:
        if re.search(keyword, text):
            return True

    # Check for excessive usage of special characters
    special_char_count = 0
    for char in text:
        if not char.isalnum() and not char.isspace():
            special_char_count += 1

    if special_char_count / len(text) > 0.1:  # more than 10% special characters
        return True

    # Text is classified as normal if no condition is met
    return False
