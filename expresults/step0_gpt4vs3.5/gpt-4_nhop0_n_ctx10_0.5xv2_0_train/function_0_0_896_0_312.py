
import re

def is_spam(message):
    # Check for common spam phrases
    spam_phrases = ["특성상", "VIP", "조작", "강력추천"]
    for phrase in spam_phrases:
        if phrase in message:
            return True
            
    # Check for URLs
    urls = re.findall('https?://(?:[-\w.]|(?:%[\da-fA-F]{2}))+', message)
    if urls:
        return True
        
    # Check for excessive use of special characters or numbers
    special_chars_percentage = sum([1 for char in message if not char.isalpha()]) / len(message)
    if special_chars_percentage > 0.3:
        return True
    
    return False
