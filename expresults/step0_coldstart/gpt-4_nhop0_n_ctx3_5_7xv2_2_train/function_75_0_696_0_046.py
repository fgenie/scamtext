def is_spam(message: str) -> bool:
    import re
    
    # Check for presence of URLs
    url_pattern = re.compile(r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*.\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+')
    if url_pattern.search(message):
        return True
    
    # Check if message contains specific spam keywords or phrases
    spam_keywords = ['외.선.물.', '일타강사진의', '미국 나스닥', '2차전지', '리튬', '반도체', '에코프로']
    for keyword in spam_keywords:
        if keyword in message:
            return True
            
    # Check for the possibility that the message is an advertisement
    ad_pattern = re.compile(r'\(광고\)')
    if ad_pattern.search(message):
        return True
    
    return False