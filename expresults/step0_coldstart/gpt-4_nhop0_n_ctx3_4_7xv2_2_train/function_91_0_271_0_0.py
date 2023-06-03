def is_spam(message):
    import re

    # Define spam keywords commonly found in spam messages
    spam_keywords = [
        '부업',
        '참여',
        '원 수익률',
        '무료체험',
        '추천주',
        '실력으로 입증',
        '성공',
        '상한가',
        '정보방',
        '초대해드립니다',
        'VIP투자반',
        '연혁',
        '타점',
        '분석',
        '종목상담',
    ]

    # Check if message contains shortening/masked URL
    url_pattern = re.compile(r'(https?:\/\/\S+)')
    has_url = bool(url_pattern.search(message))

    # Flag to check if message is spam
    is_spam = False

    # Check if message contains any spam keyword
    for keyword in spam_keywords:
        if keyword in message:
            is_spam = True
            break

    # If message contains an url and has spam keywords, then it is considered spam
    if has_url and is_spam:
        return True

    return False