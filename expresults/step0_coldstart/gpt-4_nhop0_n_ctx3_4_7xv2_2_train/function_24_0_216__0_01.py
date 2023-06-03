def is_spam(message):
    # Check for indicators of spam messages
    spam_keywords = ['상한가', '체험반', '수익률', '검증된', '종목상담', '단독제휴협약', '인수합병', '사업본격화']
    has_url = 'https://' in message
    keyword_count = sum([1 for keyword in spam_keywords if keyword in message])

    # If the message has a URL and contains one or more spam keywords, classify it as spam
    if has_url and keyword_count > 0:
        return True
    else:
        return False