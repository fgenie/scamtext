def is_spam(message):
    import re

    # Check for suspicious keywords
    spam_keywords = ['수익', '혜택', '체험반', '안전', 'VIP', '종목']
    
    for keyword in spam_keywords:
        if keyword in message:
            return True

    # Check for URLs
    url_pattern = re.compile(r"http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!* \(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+")
    
    if url_pattern.search(message):
        return True

    # Check for short links
    short_links_pattern = re.compile(r"me2\.kr/[\w]+")
    
    if short_links_pattern.search(message):
        return True

    # Check for phone numbers
    phone_pattern = re.compile(r"\d{2,4}-\d{3,4}-\d{4}|\d{10,11}")
    
    if phone_pattern.search(message):
        return True

    return False