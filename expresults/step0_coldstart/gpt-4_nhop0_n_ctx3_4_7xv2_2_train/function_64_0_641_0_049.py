def is_spam(message):
    import re
    
    spam_keywords = [
        '긴급입수정보', '국내식약처', '상한가', '정식허가임박', '탈모치료제',
        '카카오톡제재', '악성광고', '텔레그램', '동일유지', '성보장'
    ]
    
    # Check for presence of urls
    urls = re.findall('https?://(?:[-\w.]|(?:%[\da-fA-F]{2}))+', message)
    if len(urls) > 0:
        return True
        
    # Check for presence of spam keywords
    for keyword in spam_keywords:
        if keyword in message:
            return True
            
    return False