
import re

def is_spam(message):
    # Check for presence of links
    url_pattern = re.compile(r'https?://\S+|www\.\S+|kakaotalk.it/\S+|me2.kr/\S+|han.gl/\S+')
    url_count = len(url_pattern.findall(message))

    # Check for special characters
    non_alpha_numeric_count = sum(not c.isalnum() for c in message)

    # Check for presence of numbers
    number_count = sum(c.isdigit() for c in message)

    # Check for presence of percentage
    percentage_count = message.count('%')

    threshold = 3

    # If message has more than a set threshold, it's most likely spam
    if (url_count > 0 
       and non_alpha_numeric_count >= threshold 
       and number_count >= threshold) or percentage_count > 0:
        return True

    return False
