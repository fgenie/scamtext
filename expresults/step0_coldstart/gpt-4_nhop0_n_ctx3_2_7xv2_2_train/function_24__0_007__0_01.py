def is_spam(message: str) -> bool:
    import re

    spam_keywords = ['추천주', '↑', '다음주', '발표예정', '상장기업', '인수소식', '정보공개']
    message_words = re.split('\W+', message)

    spam_count = 0
    for word in message_words:
        if word in spam_keywords:
            spam_count += 1
            
    if spam_count >= 2:
        return True
    return False