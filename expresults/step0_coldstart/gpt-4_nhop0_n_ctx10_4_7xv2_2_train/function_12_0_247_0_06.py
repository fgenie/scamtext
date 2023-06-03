
import re

def is_spam(message):
    message = message.lower()

    # Check for presence of specific keywords
    spam_keywords = ['광고', '환급', '지방이식', '가격유리', '입장료']
    for keyword in spam_keywords:
        if keyword in message:
            return True

    # Check for multiple urls
    urls = re.findall(r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\\(\\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', message)
    if len(urls) > 1:
        return True

    # Check for excessive message length
    if len(message) > 150:
        return True

    # Check for repeated alphabets/numbers/special characters
    if re.search(r"(.)\1{4,}", message):
        return True

    return False
