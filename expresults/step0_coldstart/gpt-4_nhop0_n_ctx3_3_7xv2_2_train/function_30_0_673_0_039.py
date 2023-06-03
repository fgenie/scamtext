def is_spam(message):
    import re
    
    # Detect typical spam features in the message content
    suspicious_words = ['광고', '적중', '차익방법', '성과', '조각구매', '자본지원금', '하루']
    spammy_chars_regex = r'[=★]'
    url_regex = r'(http|https):\/\/(\S*|\S*[a-zA-Z0-9])'
    
    # Calculate suspicious words count
    suspicious_count = 0
    for word in suspicious_words:
        if word in message.lower():
            suspicious_count += 1

    # Check if there are too many spammy characters
    spammy_chars_count = len(re.findall(spammy_chars_regex, message))
    
    # Check if there is a URL in the message
    has_url = bool(re.search(url_regex, message))

    if suspicious_count > 1 or spammy_chars_count >= 1 or has_url:
        return True
    else:
        return False