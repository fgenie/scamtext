
import re

def is_spam(message):
    # Check for common spam phrases and patterns
    spam_phrases = ["오픈하겠습니다", "상승 확정", "기업세력이", "거래량 7배", "당신은 이것을 놓치지 않고", "절대로 손실 없는"]
    
    for phrase in spam_phrases:
        if phrase in message:
            return True
    
    # Check for consecutive special characters
    if re.search(r"[!@#$%^&*(),.?\"':{}|<>-]{2,}", message):
        return True
        
    # Check for excessive capitalization
    capital_letter_ratio = sum(1 for c in message if c.isupper()) / len(message)
    if capital_letter_ratio > 0.5:
        return True

    # Check for too many URLs
    url_count = len(re.findall(r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', message))
    if url_count > 3:
        return True

    return False
