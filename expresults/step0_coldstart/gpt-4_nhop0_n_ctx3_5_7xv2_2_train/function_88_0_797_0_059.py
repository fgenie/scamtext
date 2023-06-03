def is_spam(message):
    spam_indicators = [
        '무료',
        '체험',
        'VIP',
        '신규',
        '쿠폰',
        '출금',
        '혜택',
        '웹 그룹',
        '상상그룹'
    ]

    for indicator in spam_indicators:
        if indicator in message:
            return True

    # Check for URLs
    if "http" in message or ".com" in message or "me2.kr" in message:
        return True

    return False