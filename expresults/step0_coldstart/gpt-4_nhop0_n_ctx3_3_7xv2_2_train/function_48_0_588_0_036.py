def is_spam(message):
    spam_keywords = ['목표달성', '추천', '정회원방', '리뉴얼', '이용']
    spam_url_keywords = ['me2.kr', 'opcn-kakao.com']

    message_words = message.split(' ')

    # Check for spam keywords
    for word in message_words:
        for keyword in spam_keywords:
            if keyword in word:
                return True

    # Check for spam URLs
    for keyword in spam_url_keywords:
        if keyword in message:
            return True

    return False