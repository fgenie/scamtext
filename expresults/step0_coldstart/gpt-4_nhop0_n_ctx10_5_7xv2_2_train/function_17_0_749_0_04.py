def is_spam(message):
    import re

    # pattern for common spam characteristics
    patterns = [
        r'[0-9]{2,}%',
        r'https?://.+',
        r'무료.+거부',
        r'\d{1,2}[,]\d{3}원',
        r'특가',
        r'할인',
        r'[0-9]+분마다',
        r'상담하기',
    ]

    for pattern in patterns:
        if re.search(pattern, message):
            return True

    return False