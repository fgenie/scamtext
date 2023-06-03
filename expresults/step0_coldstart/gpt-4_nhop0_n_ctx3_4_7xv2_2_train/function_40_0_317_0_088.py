
import re

def is_spam(message):
    # Check for suspicious phrases
    phrases = ["2주안으로 최소", "상한가달성", " 상승 확정입니다", "절대 강요드리지 않습니다", "매수세 포착종목이므로", "장담합니다"]
    for phrase in phrases:
        if phrase in message:
            return True
    
    # Check for excessive use of special characters
    special_chars = "._%+-*/(){}[]|<>"
    count = sum([1 for c in message if c in special_chars])
    if count > len(message) * 0.1: # if more than 10% of the message contains special characters
        return True
    
    # Check for excessive use of capital letters
    count = sum([1 for c in message if c.isupper()])
    if count > len(message) * 0.3: # if more than 30% of the message contains capital letters
        return True
    
    # Check for suspicious URLs without context
    urls = re.findall('https?://(?:[-\w.]|(?:%[\da-fA-F]{2}))+', message)
    if len(urls) > 1:
        return True

    return False
