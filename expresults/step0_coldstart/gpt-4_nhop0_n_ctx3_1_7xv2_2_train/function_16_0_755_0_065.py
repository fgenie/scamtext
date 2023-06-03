def is_spam(message):
    import re
    
    keywords = ['부업', '수익', '참여', '지니', '틱스', '종목', '성투', '만들기', '상담', '안전']
    url_pattern = re.compile(r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+')
    
    found_keywords = sum([1 for keyword in keywords if keyword in message])
    found_urls = len(url_pattern.findall(message))
    
    if found_keywords > 0 or found_urls > 0:
        return True
    else:
        return False