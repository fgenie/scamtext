def is_spam(message):
    import re
    
    spam_keywords = ['수익', '추천', '체험반', '종목', '공개', '이익', '분석']
    short_url_patterns = ['https://me2.kr/', 'https://bit.ly/', 'https://goo.gl/']
    
    # Check for short URL
    for pattern in short_url_patterns:
        if pattern in message:
            return True
            
    # Check for spam keywords
    keyword_count = 0
    for keyword in spam_keywords:
        keyword_count += message.count(keyword)
        
    if keyword_count > 1:
        return True
        
    return False