def is_spam(message: str) -> bool:
    import re

    # Check for specific words, phrases or special characters usually found in spam messages
    spam_keywords = ['광고', '무료거부', 'kakaotalk.it']
    for word in spam_keywords:
        if word in message:
            return True

    # Check for URLs with suspicious domains
    url_pattern = re.compile(r'http(s)?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+')
    urls = url_pattern.findall(message)

    spam_domains = ['han.gl']
    for url in urls:
        for domain in spam_domains:
            if domain in url:
                return True

    # Check for unusual capitalization or excessive use of special characters
    capital_letters = sum(1 for c in message if c.isupper())
    total_letters = sum(1 for c in message if c.isalpha())
    special_chars = sum(1 for c in message if not c.isalnum() and not c.isspace())

    if total_letters > 0 and (capital_letters / total_letters) > 0.5:
        return True

    if special_chars > len(message) * 0.3:
        return True

    # If none of the above conditions are met, it's probably a normal message
    return False