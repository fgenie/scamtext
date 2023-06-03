def is_spam(message):
    import re

    # Check for multiple consecutive special characters
    if re.search(r"[\W]{2,}", message):
        return True
    
    # Check for excessive percentage symbols or number followed by a percentage symbol (indicative of stock spam)
    if len(re.findall(r"%", message)) > 1 or re.search(r"\d{1,}%\W", message):
        return True
        
    # Check for URLs with uncommon domain types indicative of spam
    if re.search(r"http(s)?://\S+\.(me2|bit)\S*", message):
        return True
    
    # Check for presence of at least 2 numbers in a message
    if len(re.findall(r"\d", message)) >= 2:
        return True

    return False