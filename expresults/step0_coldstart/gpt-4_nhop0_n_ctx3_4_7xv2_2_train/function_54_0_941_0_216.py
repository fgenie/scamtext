
import re

def is_spam(message):
    # Check for spam features such as consecutive special characters, percentage or unlikely urls
    consecutive_special_characters = re.search(r'[\!@#\$%&\*\(\)-_+={}[\]\|;:\'\",.<>/?]{2,}', message)
    percentage_sign = message.count('%') >= 3
    spam_url = re.search(r'(https?:\/\/(?:www\.)?)(me2.kr|openkakao.at|han.gl)', message)

    # Return True if any of the spam features are found
    if consecutive_special_characters or percentage_sign or spam_url:
        return True

    return False
