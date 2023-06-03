
import re

def is_spam(message):
    """
    This function takes a string 'message' as input and returns True if it is a spam message, False otherwise.
    """
    
    # Check if the message contains common spam keywords
    spam_keywords = ['원', '퍼', '지급', '메주', '부업', '참여', '보증', '공원', '이사비', '쳣', '루징', '양득', '단폴']
    for keyword in spam_keywords:
        if keyword in message:
            return True
    
    # Check if the message contains strange URLs
    url_pattern = r'\b(?:http|https|www\.|abit\.ly)\S+'
    urls = re.findall(url_pattern, message, flags=re.IGNORECASE)

    if urls:
        return True

    # Check for non-Korean characters and unusual repetitions of characters
    non_korean_pattern = r'[a-zA-Z0-9+\s\W+]+'
    non_korean = re.findall(non_korean_pattern, message)
    if len(non_korean) >= 2:
        return True

    # Check for unusual capitalization
    capitalization_pattern = r'[A-ZÀ-ẞ]{2,}'
    capitalization = re.findall(capitalization_pattern, message)
    if capitalization:
        return True
    
    # If none of the conditions are met, the message is not spam
    return False
