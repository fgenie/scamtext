
import re

def is_spam(text):
    # Define some spam indicators
    spam_indicators = ['광고', '% 적중', 'https', '원 마감', '지원금']
    
    # Define a threshold to consider a message as spam
    spam_threshold = 2
    
    # Count the occurrence of spam indicators in the message
    count = 0
    for indicator in spam_indicators:
        if indicator in text:
            count += 1
            
    # Check if the count surpasses the spam threshold
    if count >= spam_threshold:
        return True
    else:
        return False
