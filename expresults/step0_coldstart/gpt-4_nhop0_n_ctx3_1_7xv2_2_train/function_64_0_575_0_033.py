
import re

def is_spam(message):
    spam_keywords = ['지니틱스', '나노 수익', '선 물 거 래', '일평 균', '엠바고', '국내식약처', '최소3연상']
    url_pattern = r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\\(\\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+'

    # Check if message contains spam keywords
    for keyword in spam_keywords:
        if keyword in message:
            return True
            
    # Check if message contains suspicious URLs
    urls = re.findall(url_pattern, message)
    if urls:
        for url in urls:
            if not ('naver' in url or 'kakao' in url):
                return True
                
    return False
