def is_spam(message: str) -> bool:
    import re

    # Check for URL shorteners
    url_shorteners = ['bit.ly', 'tinyurl.com', 'goo.gl', 'is.gd', 't.co', 'dlvr.it', 'ow.ly', 'buff.ly', 'adf.ly', 'tiny.cc', 'shorte.st', 'tr.im', 'post', 'x.co', 'trib.al', 'opcn-kakao.com', 'vvd.bz', 'ko.gl']
    for shortener in url_shorteners:
        if shortener in message:
            return True

    # Check for phone numbers
    phone_pattern = re.compile(r'\d{2,4}-\d{3,4}-?\d{4}')
    if phone_pattern.search(message):
        return True

    # Check for keywords
    spam_keywords = ['수익', '입장', '정보', '단타매매', '무료거부', '계획', '비법']
    for keyword in spam_keywords:
        if keyword in message:
            return True

    # If none of the conditions above are met, the message is likely not spam
    return False