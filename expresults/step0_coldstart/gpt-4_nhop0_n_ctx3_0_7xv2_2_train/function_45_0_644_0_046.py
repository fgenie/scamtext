def is_spam(message):
    # List of spam keywords to check in the text
    spam_keywords = ['상승', '히든종목', '목표달성기념', '추천', '긴급입수정보', '상한가']
    
    # Tokenize the message into words
    words = message.split()
    
    # Check if any spam keyword is present in the message
    for word in words:
        if word in spam_keywords:
            return True
    
    # Check if URL is present in the message
    if 'https://' in message or 'http://' in message:
        return True
        
    return False