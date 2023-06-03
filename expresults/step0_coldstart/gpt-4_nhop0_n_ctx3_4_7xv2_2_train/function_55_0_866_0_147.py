
import re


def is_spam(message):
    # List of potential spam keywords
    spam_keywords = ['추천', '수익', '공개', '안전', '체험', '광고', '1:1교육', '무료거부']

    # Check for spam keywords
    for keyword in spam_keywords:
        if keyword in message:
            return True

    # Check for URLs
    url_pattern = re.compile(r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\\(\\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+')
    if url_pattern.search(message):
        return True

    # Check for special characters
    special_characters = ['|', '!', '+', '%']
    for char in special_characters:
        if char in message:
            return True

    # If none of the above checks return True, it's a normal message
    return False
