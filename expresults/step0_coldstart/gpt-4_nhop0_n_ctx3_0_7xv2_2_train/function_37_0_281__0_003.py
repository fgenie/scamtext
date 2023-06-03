def is_spam(message):
    import re

    # Keywords or phrases often found in spam messages
    spam_keywords = ['추천주', '체험반', '분석', '종목상담', '예정정보', '미리확인', '축하드립니다']
    
    # Check for urls in the message
    url_pattern = re.compile(r'(http|https)://[a-zA-Z0-9./]+')
    
    # Check for presence of any spam keywords
    contains_spam_keyword = any(keyword in message for keyword in spam_keywords)
    
    # Check for presence of URLs
    contains_url = bool(url_pattern.search(message))

    # Classify message as spam if it contains both spam keywords and URL
    return contains_spam_keyword and contains_url