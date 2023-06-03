def is_spam(message: str):
    import re
    
    # Check for web-based starting of message
    if message.startswith("[web발신]") or message.startswith("* [web발신]"):
        return True

    # Check for suspicious links
    suspect_domains = ['me2.kr', 'bit.ly']
    pattern = re.compile(f'http[s]?://(?:{"|".join(suspect_domains)})/[^\s]+')
    if re.search(pattern, message):
        return True
    
    # Check for common spam keywords
    spam_keywords = ['목표달성기념', '추천 디젠스', '실력보셨죠?', '고객님께서 요청하신']
    for keyword in spam_keywords:
        if keyword in message:
            return True

    # If none of the above spam indicators found, return False
    return False