def is_spam(message):
    import re

    # Check message length, spam messages are often longer.
    if len(message) > 70:
        return True

    # Check for URLs
    url_pattern = re.compile(r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+')
    if url_pattern.search(message):
        return True

    # Check for unicode characters
    if re.search(r'[^\x00-\x7F]+', message):
        return True

    # Check for large number of special characters or multiple line breaks
    if len(re.sub(r'[\w\s]', '', message)) > 5 or re.search('\n\n', message):
        return True

    return False