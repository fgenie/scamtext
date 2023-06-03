def is_spam(text: str) -> bool:
    import re

    # Check for presence of monetary amounts and percentage values
    money_amounts = r'[\d]+(,|.)[\d]+(\s)*(원|천원|만원|억원|%|％)'
    if re.search(money_amounts, text):
        return True

    # Check for presence of suspicious urls (e.g. short links or uncommon domains)
    suspicious_urls = r'http[s]?://(?:me2\.kr|bit\.ly|dokdo\.in)[^\s]+'
    if re.search(suspicious_urls, text):
        return True

    # Check for presence of 허가, 발표, 등, 폭등, 상승, 상한가, 작전정보, 종목, 공시
    keywords = r'(허가|발표|등|폭등|상승|상한가|작전정보|종목|공시|엠바고|최소|연상|적중|개락)'
    if re.search(keywords, text):
        return True

    # Check for presence of continuous upward arrows or emoticons like 😢
    upward_arrows_emoticons = r'(\^+|[\u2639-\U0001f645])+'
    if re.search(upward_arrows_emoticons, text):
        return True

    # Check for presence of free or advertisement 광고
    free_advertisement = r'(무료|광고)'
    if re.search(free_advertisement, text):
        return True

    # Check for presence of 반출금지걸려있네요, 게임좀, 예약불가, and 생일축하해
    normal_keywords = r'(반출금지걸려있네요|게임좀|예약불가|생일축하해)'
    if re.search(normal_keywords, text):
        return False

    return False