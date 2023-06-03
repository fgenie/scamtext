def is_spam(message):
    import re

    # Check for keywords related to spam
    spam_keywords = ['추천주', '목표달성', '종목', '실력', '적중']
    for keyword in spam_keywords:
        if keyword in message:
            return True

    # Check for excessive use of special characters
    special_chars = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')']
    special_char_count = sum(message.count(char) for char in special_chars)
    if special_char_count > len(message) * 0.3:  # if more than 30% of the message contains special characters
        return True

    # Check for the presence of URLs
    url_pattern = re.compile(r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\\(\\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+')
    urls_found = url_pattern.findall(message)
    if len(urls_found) > 0:
        return True

    return False