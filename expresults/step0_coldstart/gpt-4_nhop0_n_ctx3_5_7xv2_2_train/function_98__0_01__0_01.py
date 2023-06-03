def is_spam(message):
    spam_keywords = ['VIP', '차별화', '분석', '추천', '시황', '실력', '체험반', '공시발표', '당일기준', '기회']
    
    message_words = message.split()
    
    spamword_count = sum([word in spam_keywords for word in message_words])
    
    return spamword_count / len(message_words) > 0.3