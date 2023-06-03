
import re

def is_spam(message):
    # Check for excessive use of special characters
    special_chars = re.findall(r'[\*\.\(\)\\\-/@\[\]<>]', message)
    if len(special_chars) > 20:
        return True

    # Check for excessive use of numbers
    numbers = re.findall(r'\d+', message)
    if len(numbers) > 15:
        return True

    # Check for pattern of shortened urls
    urls = re.findall(r'(https?://[a-zA-Z0-9./]+)', message)
    if len(urls) > 5: 
        return True

    # Check for presence of keywords in the message
    keywords = ['상한가', '추천', '입장', '무료']
    for keyword in keywords:
        if keyword in message:
            return True

    return False
