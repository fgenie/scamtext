
import re

def is_spam(message: str) -> bool:
    spam_keywords = ["단타매매", "% 할인", "유튜브 경제야 놀자 TV", "전일 현황", "높은 진입 장벽", "무료거부080"]
    
    # Check for presence of multiple URLs
    urls = re.findall('(ht|f)tp(s?)\:\/\/[0-9a-zA-Z]([-._~\:/\?#\[\]@!$&\'()*+,;=%])*', message)
    
    if len(urls) >= 2:
        return True
    
    # Check for presence of spam keywords in the message
    for keyword in spam_keywords:
        if keyword in message:
            return True
    
    # Check for high ratio of special characters
    special_characters = "!@#$%^&*()_+[]{}|:\/?,.<>^=;"
    special_character_count = sum(1 for c in message if c in special_characters)
    if special_character_count / len(message) >= 0.05:
        return True
    
    return False
