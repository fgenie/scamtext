
import re

def is_spam(message):
    # Checking for monetary values
    if re.search(r'[\d,]+원', message):
        return True

    # Checking typical spam words and phrases
    spam_phrases = ['당일 출금가능', '가격이 오를지 내릴지', '예상하는 쉬운투자', '진입시점제공', '상담환영', '상한가 확정', '국내식약처 정식허가임박', '무료거부']
    
    for phrase in spam_phrases:
        if phrase in message:
            return True
    
    # Checking for suspicious URL shorteners
    if re.search(r'https?://bit\.ly|https?://me2\.kr', message):
        return True

    # This message doesn't match any of the spam criteria, so it's considered as a normal message.
    return False
