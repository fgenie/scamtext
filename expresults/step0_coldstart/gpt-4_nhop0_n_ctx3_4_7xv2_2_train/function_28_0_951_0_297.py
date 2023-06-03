def is_spam(message):
    import re

    # Check for excessive use of special characters
    special_chars = re.findall('[^a-zA-Z0-9\s]+', message)
    if len(special_chars) > 5:
        return True

    # Check for presence of a url
    url_regex = re.compile(r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+')
    if url_regex.search(message) is not None:
        return True

    # Check for message length
    if len(message) > 30:
        return True

    # If none of the above conditions are met, the message is likely normal
    return False