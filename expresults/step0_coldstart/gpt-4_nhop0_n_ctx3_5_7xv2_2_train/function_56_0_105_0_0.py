def is_spam(message):
    spam_keywords = ['VVIP', '리딩방', '최신 종목 추천', '수익', '비밀번호', '추천', '목표달성', '연혁', '차별화된 정보', 'VIP', '체험반']

    message_words = message.split()

    spam_count = 0
    for word in message_words:
        if word in spam_keywords:
            spam_count += 1

    if spam_count > 0:
        return True
    else:
        return False