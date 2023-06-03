def is_spam(message):
    import re

    # Check for unusual characters
    unusual_characters = re.compile(r'[^a-zA-Z0-9\s\.,;:\?!_\-@\'\"]')
    if unusual_characters.search(message):
        return True

    # Check for presence of multiple URLs
    url_pattern = re.compile(r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\\(\\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+')
    urls = url_pattern.findall(message)
    if len(urls) > 1:
        return True
    
    # Check for message length
    if len(message) > 200:
        return True

    # Check for excessive promises and pressure words
    pressure_words = ['세요', '꼭', '무료', '익절', '상승']
    count = sum([message.count(word) for word in pressure_words])
    if count >= 3:
        return True
    
    return False