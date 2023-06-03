
import re

def is_spam(message):
    # Check for multiple exclamation marks
    if re.search(r'!{2,}', message):
        return True

    # Check for excessive special characters
    if re.search(r'[!?.]{3,}', message):
        return True
    
    # Check for common spam phrases
    spam_phrases = ['고정수입', '생활고', '성공했어요', 'VIP체험반', '목표달성기념']
    if any(spam_phrase in message for spam_phrase in spam_phrases):
        return True
        
    # Check for shortened URLs
    short_url_pattern = r'(http|ftp|https)://([\w_-]+(?:(?:\.[\w_-]+)+))([\w.,@?^=%&:/~+#-]*[\w@?^=%&/~+#-])?'
    if re.search(short_url_pattern, message):
        return True

    return False
