
import re

def is_spam(message):
    # Check for spam patterns
    
    excessive_numbers = re.findall(r'\d+', message)
    if len(excessive_numbers) > 5:
        return True

    special_chars = re.findall(r'[!@#$%^&*(),.?":{}|<>]', message)
    if len(special_chars) > 5:
        return True

    spam_phrases = ['따라만 하세요', '상한가확정', '실력입증', '독보적인', '무료 상담']
    for phrase in spam_phrases:
        if phrase in message:
            return True

    return False
