def is_spam(message):
    spam_keywords = ['수익 보장', '투자반', '분석/추천/시황', '수익 실현']
    for keyword in spam_keywords:
        if keyword in message:
            return True
    return False