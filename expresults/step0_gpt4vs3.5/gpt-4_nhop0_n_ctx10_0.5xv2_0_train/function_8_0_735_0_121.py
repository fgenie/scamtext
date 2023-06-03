
import re

def is_spam(message):
    # regular expressions to identify spam patterns
    spam_patterns = [
        r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\\(\\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+',
        r'\b(?:광고|[0-9]*만원|[0-9]*배|[0-9]*주차).*\d+%',
        r'\b하이\b',
        r'\b(벌써|상한가).*\d+%',
        r'\b(무료|혜택|사은품|선물|(지원금))+',
        r'\d{3}(?=-)\d{3}(?=-)\d{3}'
    ]

    # loop through spam patterns and return True if any pattern is found in the message
    for pattern in spam_patterns:
        if re.search(pattern, message):
            return True

    # if no spam pattern found, return False (not spam)
    return False
