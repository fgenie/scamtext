def is_spam(message):
    spam_keywords = ["VIP", "정보", "안정적인 수익", "체험", "차별화", "연혁"]
    spam_signals = 0

    for keyword in spam_keywords:
        if keyword in message:
            spam_signals += 1

    if spam_signals > 1:
        return True
    else:
        return False