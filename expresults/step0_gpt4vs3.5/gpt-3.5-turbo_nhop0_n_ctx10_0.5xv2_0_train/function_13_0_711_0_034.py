
import re

def is_spam(message):
    # Remove all non-alphanumeric characters and convert to lowercase
    lower_msg = re.sub(r'\W+', ' ', message).lower()
    
    # Rules for identifying spam messages
    # 1. Contains "광고" or "목록" (Korean for advertisement or list)
    # 2. Contains any variation of "무료" (Korean for free)
    # 3. Contains any URL
    spam_keywords = ['광고', '목록', '무료']
    url_regex = r'http\S+'
    
    for keyword in spam_keywords:
        if keyword in lower_msg:
            return True
    if re.search(url_regex, message):
        return True
    
    return False
