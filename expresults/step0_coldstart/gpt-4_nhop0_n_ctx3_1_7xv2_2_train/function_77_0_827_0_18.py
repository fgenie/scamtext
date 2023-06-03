"""
Here's an implementation of a simple function to classify spam messages in Python. The function checks for some common characteristics of spam messages, such as excessive capitalization, presence of non-alphanumeric characters, and excessive use of special characters. Please note that this is a basic implementation and may not work perfectly for all cases.
"""

import re

def is_spam(message):
    # Check for excessive capitalization
    if sum(1 for c in message if c.isupper()) / len(message) > 0.5:
        return True

    # Check for excessive use of special characters
    if sum(1 for c in message if c in ['-', '+', '$', '*', '&']) / len(message) > 0.1:
        return True

    # Check for non-alphanumeric sequences longer than 2 characters
    if re.search('\W{3,}', message):
        return True

    # Check for commonly known spam words/phrases
    spam_words = ['상한가확정', 'MOU추친중', '체험반 다음 타자']
    for word in spam_words:
        if word in message:
            return True

    # If none of the above criteria is met, we consider the message as normal
    return False