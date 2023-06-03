
import re

def is_spam(message):
    spam_keywords = ['당첨', '참여 링크', '무료 참여', '자동 매매', '축하합니다', '준비']
    has_url_regex = r'https?://(?:[-\w.]|(?:%[\da-fA-F]{2}))+'
    excessive_whitespace = r'\s{2,}'

    # Checking if the message contains spam keywords
    if any(keyword in message for keyword in spam_keywords):
        return True
    
    # Checking if the message contains URL
    if re.search(has_url_regex, message):
        return True

    # Checking for excessive whitespace
    if re.search(excessive_whitespace, message):
        return True
    
    return False
