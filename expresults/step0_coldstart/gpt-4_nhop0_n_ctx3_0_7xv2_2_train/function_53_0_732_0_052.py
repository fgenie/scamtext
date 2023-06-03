def is_spam(message):
    import re

    spam_words = ["상승", "공개", "고효율", "FDA승인", "임상", "지원", "신약", "진입", "고급정보"]
    url_patterns = [r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\\(\\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+',
                    r'me2\.kr/[a-zA-Z0-9]+',
                    r'openkakao\.at/[a-zA-Z0-9]+']

    for word in spam_words:
        if word in message:
            return True
            
    for pattern in url_patterns:
        if re.search(pattern, message):
            return True
                
    return False