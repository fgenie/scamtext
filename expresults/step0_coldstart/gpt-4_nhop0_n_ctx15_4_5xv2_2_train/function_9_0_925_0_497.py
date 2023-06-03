def is_spam(message):
    import re

    # Spam keyword patterns
    spam_patterns = [
        r"(광고)",
        r"\d{2,}%",
        r"[ㄱ-ㅎㅏ-ㅣ가-힣]*[주식|추천|상승|하락|투자]",
        r"(상한가|하한가)",
        r"\d{1,2}월\s?체험",
        r"\d{2,3}만원",
        r"\+[가-힣]+주",
        r"\b\d{1,2}타\b",
        r"(https?:\/\/[\w\.-]+\.[\w\.-]+\/\S*)",
        r"-코인",
        r"[가-힣]+계약",
        r"(시작하세요|수익|적중|투자)+"
        r"(https?:\/\/(bit\.ly|dokdo\.in|me2\.kr|me2.do)\S*)"
    ]

    # Iterate through the spam keyword patterns
    for pattern in spam_patterns:
        if re.search(pattern, message):
            return True

    # Return False for normal messages
    return False