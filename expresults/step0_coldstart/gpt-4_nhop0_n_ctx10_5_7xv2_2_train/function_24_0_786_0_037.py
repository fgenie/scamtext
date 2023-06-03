def is_spam(message):
    import re
    spam_keywords = [
        "단타정보", "광고", "타점", "EVENT", "code", "무료거부", "공시발표",
        "체험VIP정보방", "국내선물옵션", "증권사부장출신", "미공개 공시종목", "극비 작전주",
        "쉬는시간", "청개구리VIP", "공개", "알려드린",
        "목표가", "익 절 가", "전문가 경력", "실현수익률", "누적수익률"]

    for keyword in spam_keywords:
        if keyword in message:
            return True

    url_patterns = [
        r"https?://\S+", r"bit\.ly/\S+", r"me2\.kr/\S+", r"buly\.kr/\S+",
        r"opcn-kakao\.com/\S+"]

    for pattern in url_patterns:
        if re.search(pattern, message):
            return True

    return False