
import re

def is_spam(message):
    spam_keywords = ['청개구리', 'VIP', '체험반', '차별화된', '정보', '하루', '따라만', '축하합니다', '다음', '타자', '여의도']
    normal_keywords = ['KB국민', '기업카드', '영업점', '보관', '안내', '카드', '신분증', '대표자', '대리인', '위임장']
    
    # Check for links
    link_pattern = "(https?://[_a-zA-Z0-9\-\./]+)"
    has_link = bool(re.search(link_pattern, message))
    
    # Check for common spam keywords in the message
    count_spam = sum([keyword in message for keyword in spam_keywords])
    
    # Check for common normal keywords in the message
    count_normal = sum([keyword in message for keyword in normal_keywords])
    
    if count_spam > count_normal or (has_link and count_spam > 0):
        return True
    else:
        return False
