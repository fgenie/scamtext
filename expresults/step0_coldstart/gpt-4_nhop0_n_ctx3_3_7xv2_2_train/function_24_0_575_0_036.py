import re

def is_spam(message):
    spam_patterns = [
        r'\b(광고)\b',
        r'\b(적중)\b',
        r'\d{1,4}\/\d{1,4}',
        r'https:\/\/me2\.kr\/',
        r'\b(암호)\d{4}\b',
        r'\b(무료거부)\b',
        r'\b(신년맞이)\b',
        r'\b(단타거래)\b'
    ]
    
    for pattern in spam_patterns:
        if re.search(pattern, message):
            return True
    
    return False