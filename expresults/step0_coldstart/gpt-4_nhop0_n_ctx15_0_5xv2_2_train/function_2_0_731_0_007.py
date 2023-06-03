def is_spam(message):
    spam_keywords = [
        '광고', '입장코드', '무료거부', '단체방',
        '상한가', '적중', '수익', '손실', '진입',
        '추천드릴', '체험반', '안내드립니다',
        '지금', '증권', '무 료 체 험',
        '오후', '수익률', '행복지원'
    ]

    spam_elements = 0

    for keyword in spam_keywords:
        if keyword in message:
            spam_elements += 1

    # If more than one spam keyword is found, consider it as spam
    if spam_elements > 1:
        return True

    # Check if message contains suspicious URLs
    if 'http' in message or '카>' in message:
        return True

    return False