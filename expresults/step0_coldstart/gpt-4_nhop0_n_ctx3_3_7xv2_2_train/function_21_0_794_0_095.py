
import re

def is_spam(message):
    spam_keywords = ['광고', '지원', '선물', '원', '지긋지긋한', '부터', '나스닥', '계약', '수수료', '안정적']
    spam_patterns = [
        r'\d+,\d+,\d+원',
        r'https?:\/\/\S+',
        r'입장코드:?\d+',
        r'\d+만원',
        r'\[\d+만원\]',
    ]

    message_low = message.lower()

    # Check for spam keywords    
    for keyword in spam_keywords:
        if keyword in message_low:
            return True

    # Check for spam patterns
    for pattern in spam_patterns:
        if re.search(pattern, message_low):
            return True

    return False
