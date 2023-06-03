def is_spam(message):
    import re

    # Set spam keywords and patterns
    spam_keywords = ['(광고)', '무료거부', '월20만원', '지금운신', '급등중', '추천', '모집', '접수순위', '성과', '예정', '알려드립니다', '수익률', '무료']
    spam_patterns = [
        re.compile(r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\\(\\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+'),
        re.compile(r'openkakao\.at/[^\s]+'),
        re.compile(r'me2\.kr/\S+'),
        re.compile(r'[a-zA-Z0-9\-\._]+@[a-zA-Z0-9\-\._]+\.[a-zA-Z]{2,}')
    ]

    # Check if there are any spam keywords in the message
    for keyword in spam_keywords:
        if keyword in message:
            return True

    # Check if there are any spam patterns in the message
    for pattern in spam_patterns:
        if pattern.search(message):
            return True

    return False