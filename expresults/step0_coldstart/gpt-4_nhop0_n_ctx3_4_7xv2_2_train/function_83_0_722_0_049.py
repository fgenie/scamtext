
import re

def is_spam(message):
    # defining the spam patterns
    spam_patterns = [
        r'\(광고\)',
        r'\d{4}만',
        r'무료거부',
        r'비용',
        r'계\.약\.기준',
        r'성과',
        r'http[s]?://\S+'
    ]

    # iterate through the spam_patterns and check if any of them exist in the message
    for pattern in spam_patterns:
        if re.search(pattern, message):
            return True

    # if no spam_patterns are found in the message, it is not a spam
    return False
