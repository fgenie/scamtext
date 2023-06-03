def is_spam(message):
    import re
    
    # Check for presence of URLs
    url_pattern = re.compile(r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\\(\\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+')
    urls = url_pattern.findall(message)
    if len(urls) > 0:
        return True
    
    # Check for presence of specific spam phrases and keywords
    spam_keywords = ['수익', '추천', '관망', '가져', '비번', '주주', '분석', '시황', '입맛대로', '타점', '증권']
    for word in spam_keywords:
        if word in message:
            return True
    
    # Check for excessive use of special characters
    special_char_pattern = re.compile(r'[^a-zA-Z0-9가-힣]+')
    special_chars = special_char_pattern.findall(message)
    if len(special_chars) > 4:
        return True

    # If none of the above conditions are met, the message is likely not spam
    return False