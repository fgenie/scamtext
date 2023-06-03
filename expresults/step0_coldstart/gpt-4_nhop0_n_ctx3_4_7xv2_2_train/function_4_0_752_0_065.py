
import re

def is_spam(message):
    # Check for potentially spammy phrases
    spam_phrases = [
        '적중', '추천주', '수익', '비밀번호', '종목', 'VVIP', '500%'
    ]
    
    for phrase in spam_phrases:
        if phrase in message:
            return True
    
    # Check for URLs
    url_pattern = re.compile(r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\\(\\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+')
    if url_pattern.search(message):
        return True
    
    # If none of the spam filters are triggered, it's likely a normal message.
    return False
