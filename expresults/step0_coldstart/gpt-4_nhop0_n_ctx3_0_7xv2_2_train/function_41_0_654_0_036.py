def is_spam(message):
    import re
    
    spam_words = ['실력입증', '추천주', '차익방법', '1:1멘토링', '체험반', '적중']
    pattern = r'https://[^\s]*'

    # Check for spam words
    for word in spam_words:
        if word in message:
            return True

    # Check for urls
    if re.search(pattern, message):
        if "https://" not in message.split()[:2] and "http://" not in message.split()[:2]:  # check if url is not at the beginning, common in spam messages
            return True

    return False