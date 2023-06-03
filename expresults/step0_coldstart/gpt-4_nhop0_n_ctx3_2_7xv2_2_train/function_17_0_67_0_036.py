def is_spam(message):
    import re

    spam_keywords = ["제재", "악성광고", "입장 안내", "VIP", "투자체험", "매수/매도", "시황", "추천종목"]
    pattern_url = re.compile(r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!* \(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+')

    if any(keyword in message for keyword in spam_keywords):
        return True

    if pattern_url.search(message):
        return True

    return False