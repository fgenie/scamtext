
import re

def is_spam(message):
    # Check for excessive use of special characters
    special_char_ratio = len(re.findall('[^a-zA-Z0-9가-힣\s]', message)) / len(message)
    if special_char_ratio > 0.5:
        return True
    
    # Check for excessive capitalization
    capital_ratio = len(re.findall('[A-Z]', message)) / len(message)
    if capital_ratio > 0.7:
        return True

    # Check for spammy keywords or phrases
    spammy_keywords = ['공짜', '지금입장', '매일복리', '가입금지급',
                       '한정수량', '평생수익', '무한지급', '경품',
                       '안전거래소', '무료거부', '입장코드']
    for keyword in spammy_keywords:
        if keyword in message:
            return True

    # Check for url patterns
    urls = re.findall(r'https?://[\w/:%#\$&\?\(\)~\.=\+\-]+', message)
    if urls:
        return True

    # If none of the above conditions are met, the message is not spam
    return False
