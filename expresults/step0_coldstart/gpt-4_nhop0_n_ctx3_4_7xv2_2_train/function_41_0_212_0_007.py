
import re

def is_spam(message):
    # Check for suspicious keywords that are common in spam messages
    spam_keywords = ['하루', '따라만', '최소', '코 인', '단 타', '소 액', '처음', '주1회', '전화X', '톡']

    # Check for spam URL structure and high number of special characters
    spam_urls = re.findall('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\\(\\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', message)
    special_char_count = len(re.findall('[^a-zA-Z0-9가-힣]', message))
    
    # If the message contains any of the spam keywords, treat it as spam
    if any(keyword in message for keyword in spam_keywords):
        return True
    
    # If the message has more than one spam URL and if the ratio of special characters is more than 30%, treat it as spam
    if len(spam_urls) > 1 and special_char_count / len(message) > 0.3:
        return True
    
    return False
