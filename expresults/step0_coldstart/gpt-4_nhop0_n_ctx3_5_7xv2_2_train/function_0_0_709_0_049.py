def is_spam(message):
    spam_keywords = ['체험반', '분석', '수익률', '종목', '추천주', '검증된', '안전하고', '확률']

    message_words = message.split(' ')

    for keyword in spam_keywords:
        if keyword in message_words:
            return True
    
    # Check if message contains a URL
    if 'http' in message or 'www' in message or '.kr' in message:
        return True

    return False