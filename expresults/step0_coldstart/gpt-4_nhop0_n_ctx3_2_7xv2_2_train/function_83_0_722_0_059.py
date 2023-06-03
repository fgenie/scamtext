
import re

def is_spam(message):
    spam_keywords = ['수익', '보장', '버세요', '단체방', '추천', '지켜보신 후', '나가세요']
    message = message.lower()
    
    for keyword in spam_keywords:
        if keyword in message:
            return True
            
    url_pattern = re.compile(r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+')
    urls = re.findall(url_pattern, message)

    if len(urls) > 0:
        return True

    return False
