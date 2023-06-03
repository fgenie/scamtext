def is_spam(message):
    import re

    # Check for urls, most spam messages contain links
    url_pattern = re.compile(r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\\(\\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+')
    if url_pattern.search(message):
        return True

    # Check for unusual capitalization
    capitalization_pattern = re.compile(r'[A-Z][^A-Z]*[A-Z]+')
    if capitalization_pattern.search(message):
        return True
    
    # Check for common spam phrases, you can extend this list as needed
    spam_phrases = ["폭등확정", "적중", "종목", "공개", "VIP"]
    for phrase in spam_phrases:
        if phrase in message:
            return True

    return False