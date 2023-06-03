def is_spam(message):
    import re

    spam_keywords = ['추천', '상승', '무료', '원금', '현황', '수수료', '재료비', '투자', '입금', '출금',
                     '성공', '페어', '조각구매', '지급', '성과', '↓함께', '지급중', '혜택', '부업', '고정수입',
                     'VIP', '적중', '광고']

    # Check for common spam keywords
    for keyword in spam_keywords:
        if keyword in message:
            return True

    # Check for URL in message
    url_pattern = re.compile(r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\\(\\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+')
    if url_pattern.search(message):
        return True

    # Check for phone numbers
    phone_pattern = re.compile(r'\d{2,4}-\d{3,4}-\d{4}')
    if phone_pattern.search(message):
        return True

    return False