def is_spam(message):
    import re

    # Check for URL patterns
    url_pattern = re.compile(r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\\(\\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+')
    if url_pattern.search(message):
        return True
    
    # Check for phone numbers
    phone_pattern = re.compile(r'(\+\d{1,4}(\s|-)?)?(\d{1,4}(-|\s)?){2,}\d{2,}')
    if phone_pattern.search(message):
        return True
    
    # Check for keywords commonly used in spam messages
    spam_keywords = ['[%]', '수익달성', '인증']
    for keyword in spam_keywords:
        if keyword in message:
            return True
    
    return False