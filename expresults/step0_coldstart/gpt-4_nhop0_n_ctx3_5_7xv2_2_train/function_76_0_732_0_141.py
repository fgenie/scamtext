def is_spam(message):
    import re

    # Check for presence of multiple consecutive special characters
    if re.search(r'[\W_]{4,}', message):
        return True

    # Check for multiple consecutive uppercase words
    if re.search(r'([A-Z]{2,}\s*){2,}', message):
        return True

    # Check for suspicious URLs
    suspicious_urls = ['me2.kr', '투자지원방.com']
    for url in suspicious_urls:
        if url in message:
            return True

    # Check for large numerical values in the message
    if re.search(r'\d{5,}', message):
        return True

    return False