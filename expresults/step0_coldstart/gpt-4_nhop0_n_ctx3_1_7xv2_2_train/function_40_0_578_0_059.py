
import re

def is_spam(message):
    # Checks for multiple ellipsis (..) and excessive exclamation marks (!!).
    if re.search(r"\.{2,}", message) or re.search(r"!{2,}", message):
        return True
    
    # Checks for URL shortening services in the message.
    shorteners = ['bit.ly', 'goo.gl', 'tinyurl.com', 'ow.ly', 't.co', 'me2.kr', 'han.gl']
    for shortener in shorteners:
        if shortener in message:
            return True

    # Checks for common spam phrases in the message.
    spam_phrases = [
        '빠르게 입장해 주세요',
        '비용요구, 가입 등 일절 없습니다',
        '정보만 있다면 절대 파란불 발생하지 않습니다',
        '현재 상황에 따라 적극대응 하시며'
    ]
    for phrase in spam_phrases:
        if phrase in message:
            return True
    
    return False
