def is_spam(message):
    import re
    
    # Check if message contains the word "광고" (advertisement)
    if "광고" in message:
        return True
    
    # Check if message contains a typical url pattern with special characters
    if re.search("http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\\(\\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+", message):
        return True

    # Check if message contains numbers separated by commas (e.g., 4일+449만)
    if re.search("\d{1,3}(?:-\d{3})*(\,\d{1,3}(?:-\d{3})*)*(\+\d{1,3}(?:-\d{3})*)*", message):
        return True

    # Check if message contains suspicious domain like ".in" or ".kr"
    if re.search("\.in|\.kr", message):
        return True

    return False