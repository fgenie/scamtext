def is_spam(message):
    import re

    spam_keywords = [
        "광고",
        "해외선물",
        "지원금",
        "계약",
        "주식",
        "로또"
    ]
    
    spam_url_shorteners = [
        "dokdo.in",
        "han.gl",
        "t.ly"
    ]

    # Check for presence of spam keywords
    for keyword in spam_keywords:
        if keyword in message:
            return True

    # Check for presence of shortened urls
    for url_shortener in spam_url_shorteners:
        if url_shortener in message:
            return True

    # Check for presence of long numbers
    long_numbers = re.findall(r'\d{5,}', message)
    if long_numbers:
        return True

    return False