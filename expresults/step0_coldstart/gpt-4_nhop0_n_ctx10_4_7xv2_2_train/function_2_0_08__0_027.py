
import re

def is_spam(message):
    keywords = ['click', 'free', 'win', 'register', 'money', 'success', '당첨', '수익', '원금']
    spam_score = 0
    
    # Check for multiple exclamation marks
    if re.search('!!+', message):
        spam_score += 1
    
    # Check for multiple links
    links = re.findall(r'https?://[^\s]+', message)
    if len(links) > 1:
        spam_score += 1
    
    for keyword in keywords:
        if keyword in message.lower():
            spam_score += 1
    
    # Update this threshold as needed.
    if spam_score >= 2:
        return True
    
    return False
