import re

def is_spam(message: str) -> bool:
    spam_words = ['비밀번호', '손실', '회의원', '%', '↑', '공유', '정보', '클릭', '체험반', '추천주', '상한가',
                  '종목 오즈피아', '증권', '채널', '리포터', '지금50%', '상승', '상한가', '익절']
    
    message_lowercase = message.lower()
    
    # Checking for spam words in the message
    for word in spam_words:
        if word in message_lowercase:
            return True
        
    # Checking for URLs in the message
    url_pattern = re.compile(r'(http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\\(\\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+)')
    if url_pattern.search(message):
        return True
        
    return False