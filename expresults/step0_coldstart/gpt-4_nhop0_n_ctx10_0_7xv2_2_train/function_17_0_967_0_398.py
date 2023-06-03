def is_spam(message):
    import re

    # Check for typical spam words and phrases
    spam_words = ['광고', '링크', '지원금', '비용', '방안내', '무료거부', '추천', '수익', '실현', '단타거래', '종목', '체험반', '무료로']
    for word in spam_words:
        if word in message:
            return True

    # Check for urls
    url_count = len(re.findall(r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', message))
    if url_count > 1:
        return True

    # Check for special characters
    if re.search(r"[^\w\s,.]", message):
        return True

    # Check for specific message patterns
    if '-너도나도' in message or '단체방' in message or '최근 3개월 매매' in message:
        return True

    return False