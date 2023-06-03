
import re

def is_spam(message):
    message = message.lower()

    # Rule 1: Check for suspicious words or phrases, e.g. '축하합니다', '안내입니다', '상승 확정', '오픈하겠습니다'
    spam_phrases = ['축하합니다', '안내입니다', '상승 확정', '오픈하겠습니다']
    for phrase in spam_phrases:
        if phrase in message:
            return True
    
    # Rule 2: Check for short url services, e.g. me2.kr, openkakao.io
    url_pattern = re.compile('(?:http|https)>?[.:]{2,}\\S+(?:\\/(?![a-zA-Z_z-])+)?$')
    if url_pattern.search(message):
        shortened_url_services = ['me2.kr', 'openkakao.io']
        for service in shortened_url_services:
            if service in message:
                return True
    
    # Rule 3: Check for excessive use of special characters, e.g. |, <, >
    special_chars = ['|', '<', '>']
    char_count = 0
    for char in special_chars:
        char_count += message.count(char)
    
    if char_count > 2:
        return True
    
    return False
