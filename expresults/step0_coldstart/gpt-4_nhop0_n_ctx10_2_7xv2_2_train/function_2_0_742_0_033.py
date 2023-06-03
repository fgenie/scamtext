def is_spam(message):
    import re
    
    message = message.lower()
    
    # Check for spam keywords
    spam_keywords = [
        "vip체험반", "신규", "출금", "혜택", "중계", "적중",
        "단타정보트레이딩", "주식공시", "회사공시",
        "익 절 가", "수익률", "편입가", "목표가",
        "전문가 경력", "증권사", "애널리스트", "실전투자대회",
        "단타종목", "차익방법", "1:1멘토링",
        "종목확인", "카톡방", "실력입증", "추천주"
    ]
    
    for keyword in spam_keywords:
        if keyword in message:
            return True
    
    # Check for URL patterns
    url_patterns = [
        r"http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\\(\\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+",
        r"openkakao.io/[a-zA-Z0-9]+",
        r"me2.kr/[a-zA-Z0-9]+",
        r"dokdo.in/[a-zA-Z0-9]+",
        r"opcn-kakao.com/[a-zA-Z0-9]+",
        r"mpp23.com",
    ]

    for pattern in url_patterns:
        if re.search(pattern, message):
            return True
    
    return False