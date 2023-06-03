def is_spam(message):
    import re

    spam_keywords = [
        '광고', '해외선물', '매매강의', '무료거부', '적중', '카카오톡제재', '악성광고', '텔레그램'
    ]
    
    message = message.strip()
    
    # check for urls with shortening services
    short_urls = re.findall(r'https?://me2\.kr/\w+', message)
    if short_urls:
        return True

    # check for multiple special characters
    special_chars = re.findall(r'[!@#$%^&*()_+=|<>?{}[]\;:,./]+', message)
    if len(special_chars) > 3:
        return True

    # check for spam keywords
    for keyword in spam_keywords:
        if keyword in message:
            return True
    
    return False