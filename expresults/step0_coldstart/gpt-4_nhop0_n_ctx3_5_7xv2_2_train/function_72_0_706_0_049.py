
import re

def is_spam(text):
    # Set spam thresholds
    url_threshold = 1
    consecutive_caps_threshold = 5
    
    # Check for URL patterns
    urls = re.findall(r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', text)
    if len(urls) >= url_threshold:
        return True

    # Check for excessive use of consecutive capital letters
    consecutive_caps = re.findall(r'[A-Z]{%d,}' % consecutive_caps_threshold, text)
    if len(consecutive_caps) > 0:
        return True

    # Check for spam keywords
    spam_keywords = ['광고', '무료거부', 'Event', '추천주']
    for keyword in spam_keywords:
        if keyword in text:
            return True
    
    return False
