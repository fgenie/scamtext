
import re

def is_spam(message):
    # Check for URL patterns
    url_patterns = [r'openkakao\.io', r'me2\.kr']
    for pattern in url_patterns:
        if re.search(pattern, message):
            return True
    
    # Check for suspicious phrases
    suspicious_phrases = [r'입장 안내 드립니다', r'실력입증', r'추천주', r'상한가확정']
    for phrase in suspicious_phrases:
        if re.search(phrase, message):
            return True
    
    return False
