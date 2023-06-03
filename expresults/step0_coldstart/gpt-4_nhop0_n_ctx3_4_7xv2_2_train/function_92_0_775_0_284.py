
import re

def is_spam(message):
    # Check for URLs
    url_pattern = re.compile(r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\\(\\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+')
    if url_pattern.search(message):
        return True

    # Check for keywords
    keywords = ["최소", "매도", "프리미엄", "사탕"]
    for keyword in keywords:
        if keyword in message:
            return True

    # Check for non-alphanumeric characters
    non_alphanumeric_count = sum([c.isalnum() == False for c in message])
    if non_alphanumeric_count / len(message) > 0.3:
        return True

    return False
