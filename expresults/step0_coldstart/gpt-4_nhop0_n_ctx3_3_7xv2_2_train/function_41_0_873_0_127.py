
import re

def is_spam(message):
    # Check for excessive use of special characters
    if len(re.findall(r'[!@#$%^&*()-_=+{}\[\];:"/<>?]', message)) > 5:
        return True
    
    # Check for presence of URLs
    if re.search(r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\\(\\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', message) is not None:
        return True

    # Check for presence of typical spam keywords
    spam_keywords = ['광고', '시간내서', '변할수', '있습니다', '선물', '사람처럼', '한번쯤은', '자유롭게', '해선지원금혜택']
    if any(keyword in message for keyword in spam_keywords):
        return True

    return False
