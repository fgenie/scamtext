
import re

def is_spam(message):
    # Check for shortened links like me2.kr
    if re.search(r'https?://\w{1,5}\.\w{2,3}', message):
        return True

    # Check for high percentage values (indicating false promises of gains)
    if re.search(r'\d{2,3}%\s?(?:상승|돌파|고효율)', message):
        return True

    # Check for consecutive special characters (indicating false urgency)
    if re.search(r'[\!\*]{2,}', message):
        return True

    # Check for stock recommendation-like phrases (indicating potential scams)
    if re.search(r'(상한가확정|추천주|M반도체)', message):
        return True
    
    return False
