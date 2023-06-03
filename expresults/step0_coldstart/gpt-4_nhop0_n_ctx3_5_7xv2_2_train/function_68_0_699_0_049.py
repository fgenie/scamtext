
import re

def is_spam(message):
    # Check for ad/spam indicators
    ad_indicators = ['(광고)', '무료패키지', '무료거부', '【', '】', '▶', 'http']
    words = message.split(' ')
    
    # Check if any ad indicators are present in the message
    for word in words:
        if any(indicator in word for indicator in ad_indicators):
            return True

    # Check for URLs
    urls = re.findall('https?://(?:[-\w.]|(?:%[\da-fA-F]{2}))+', message)
    if urls:
        return True
    
    return False
