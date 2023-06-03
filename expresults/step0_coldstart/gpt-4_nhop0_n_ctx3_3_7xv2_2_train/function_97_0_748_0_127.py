def is_spam(message: str):
    import re
    
    # Define spam related keywords
    spam_keywords = ['광고', '추가Event', '해외선물', '챗 GPT']

    # URL pattern regex
    url_pattern = re.compile(r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+')

    # Check if message contains spam keywords
    if any(keyword in message for keyword in spam_keywords):
        return True
    
    # Check if message contains excessive urls
    if len(url_pattern.findall(message)) > 1:
        return True
        
    # Check if the message contains phone numbers or codes
    if re.search(r'\d{2,}', message):
        return True

    return False