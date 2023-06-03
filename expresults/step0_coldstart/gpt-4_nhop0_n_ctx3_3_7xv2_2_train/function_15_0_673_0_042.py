
import re

def is_spam(message):
    spam_keywords = ['축하합니다', '클릭', '투자반', '식약처', '오파스넷', '정식허가임박']
    normal_keywords = ['먹었냐', '한잔', '오늘중', '사무실']
    
    # Check for spam keywords
    for keyword in spam_keywords:
        if keyword in message:
            return True
            
    # Check for normal keywords
    for keyword in normal_keywords:
        if keyword in message:
            return False
            
    # Check for URLs without the normal keywords
    url_pattern = r'https?://\S+'
    if re.search(url_pattern, message) and not any(keyword in message for keyword in normal_keywords):
        return True

    return False
