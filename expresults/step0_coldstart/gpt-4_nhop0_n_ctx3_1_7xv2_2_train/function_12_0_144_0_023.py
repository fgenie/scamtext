
def is_spam(message):
    spam_keywords = ['광고', '아래 주소', '체계적 학공', '안정적인 HTS', '수수료', '입장코드', '무료거부', '바로 증정']
    
    message_lower = message.lower()
    
    for keyword in spam_keywords:
        if keyword.lower() in message_lower:
            return True
            
    return False
