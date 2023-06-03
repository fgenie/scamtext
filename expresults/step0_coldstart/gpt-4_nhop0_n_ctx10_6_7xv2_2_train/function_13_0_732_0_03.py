
import re

def is_spam(message):
    if re.search(r'http[s]?://[a-zA-Z0-9./?=_%:-]*', message):
        return True
    
    if re.search(r'[\d]+%', message):
        return True
    
    if re.search(r'(목표달성)|(고지료)|(바쁜 시간)|(증여세)|(청개구리)', message):
        return True

    return False
