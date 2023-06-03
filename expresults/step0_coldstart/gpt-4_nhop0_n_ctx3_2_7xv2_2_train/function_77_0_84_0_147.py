def is_spam(message):
    import re

    # Check for keywords that are likely to appear in spam messages
    spam_words = ['VIP체험반', '추천', '참여', '차별화된 정보', '공시발표 전 단독입수한 종목', '다음타자 이어서 공개']
    for word in spam_words:
        if word in message:
            return True

    # Check for URL shorteners, which are commonly used in spam messages
    if re.search(r'https?://(me2\.kr|bit\.ly|goo\.gl|tinyurl\.com)', message):
        return True

    # Check for unusual patterns of characters, such as numbers mixed with letters
    if re.search(r'[가-힣]+[0-9]+', message) or re.search(r'[0-9]+[가-힣]+', message):
        return True

    return False