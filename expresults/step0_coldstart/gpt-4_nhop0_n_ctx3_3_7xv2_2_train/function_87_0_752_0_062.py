
import re

def is_spam(message):
    # Check for presence of URL
    url_pattern = 'https?://(?:[-\w.]|(?:%[\da-fA-F]{2}))+'
    if re.search(url_pattern, message):
        return True

    # Check for presence of unusual symbols such as |
    unusual_symbols = ['|']
    for symbol in unusual_symbols:
        if symbol in message:
            return True

    # Ignore case when analyzing the text
    message = message.lower()

    # List of spam-related keywords
    spam_keywords = ['무료', '체험반', '강판', '독점', '공급', '발표시', '상한가', '추천주', '알미늄']

    for keyword in spam_keywords:
        if keyword in message:
            return True

    return False
