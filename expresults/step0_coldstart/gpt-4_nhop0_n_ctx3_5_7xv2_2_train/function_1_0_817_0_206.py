
import re

def is_spam(message):
    url_pattern = r'https?:\/\/(?:[-\w.]|(?:%[\da-fA-F]{2}))+'
    unusual_characters = r'[!^&%$#~{};_\*\[\]:|]'

    if re.search(url_pattern, message) or re.search(unusual_characters, message):
        return True
    else:
        return False
