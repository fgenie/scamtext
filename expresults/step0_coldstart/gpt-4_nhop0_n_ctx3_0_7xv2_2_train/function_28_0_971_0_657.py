def is_spam(message):
    import re

    # Check for excessive special characters, capital letters or digits
    if re.search(r'[^a-zA-Z0-9\s]{4,}', message) or re.search(r'[A-Z]{4,}', message) or re.search(r'\d{4,}', message):
        return True

    # Check for specific terms
    spam_terms = ['추천주', '양방', '배당지급','상한가','vip','원할인', '체험반', '사업본격화', '약속합니다', '선착순', '차별화된 정보', '광고', '할인']
    for term in spam_terms:
        if term in message:
            return True

    # Check for suspicious urls
    urls = re.findall(r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\\(\\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', message)
    if urls:
        for url in urls:
            if re.search(r'(me2\.kr)|(☞)|(ⓒ)|(bz)|(bv)|(baf)', url):
                return True

    return False