
import re

def is_spam(message):
    if len(message) > 50:
        return True

    if re.search(r'\d+(\*|~)[a-zA-Z]*', message):
        return True

    if message.startswith("(광고)") or message.startswith("▼클릭") or message.startswith("무료거부"):
        return True

    if re.search(r'(https?:\/\/\S+)', message):
        return True

    return False
