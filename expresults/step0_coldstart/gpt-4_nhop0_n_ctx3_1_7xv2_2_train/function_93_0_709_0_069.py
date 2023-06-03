
import re

def is_spam(message):
    # Convert the message to lowercase for better comparison
    message = message.lower()
 
    # Pattern for detecting the key features typically used in spam messages
    spam_patterns = [
        r'\d{1,2}월',
        r'\d+\.{0,1}\d+원',
        r'\d+\,{0,1}\d+장',
        r'\d+[0-9a-zA-Z]{1}배',
        r'https?:\/\/\S+',
        r'AI 자동 매매',
        r'무료 참여',
        r'\S*체험반',
    ]
    for pattern in spam_patterns:
        if re.search(pattern, message):
            return True

    return False
