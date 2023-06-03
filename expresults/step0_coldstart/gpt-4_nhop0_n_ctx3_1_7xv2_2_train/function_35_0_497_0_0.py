def is_spam(text: str) -> bool:
    import re
    
    # Check if message contains url with spammy patterns
    urls = re.findall(r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\\(\\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', text)
    spammy_url_patterns = ['me2.kr']
    
    for url in urls:
        for pattern in spammy_url_patterns:
            if pattern in url:
                return True
                
    # Check for spammy words and phrases
    spammy_keywords = ["추천주", "%p↑", "세토피아", "여의도", "체험반", "단타정보트레이딩"]
    
    for keyword in spammy_keywords:
        if keyword in text:
            return True
    
    # Random emojis
    emojis = re.findall(r'[\U0001F600-\U0001F64F]', text)
    if len(emojis) > 4:
        return True
  
    # Default case: not spam
    return False