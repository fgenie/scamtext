def is_spam(message):
    import re
    
    # Check for presence of URL shorteners
    url_shortener_pattern = re.compile(r'http(s)?:\/\/(me2\.kr|bit\.ly|goo\.gl|tinyurl\.com)\/\S+')
    if re.search(url_shortener_pattern, message):
        return True
    
    # Check for presence of excessive special characters or numbers
    special_chars_pattern = re.compile(r'[\W\d]{4,}')
    if re.search(special_chars_pattern, message):
        return True
    
    # Check for keywords related to spam
    spam_keywords = ['지급', '나노 수익', '안전하고 확률', '꿀팁', '비결', '벳썸']
    for keyword in spam_keywords:
        if keyword in message:
            return True

    # If none of the conditions above are met, classify the message as normal
    return False