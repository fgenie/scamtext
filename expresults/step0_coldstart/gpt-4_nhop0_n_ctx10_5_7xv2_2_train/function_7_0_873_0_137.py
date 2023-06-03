def is_spam(message):
    import re

    # Check for common spam phrases
    spam_phrases = [
        "수익달성", "무료체험반", "부자가", "청개구리", "거부 080", "바이오", "상승", "히든종목",
        "신규회원", "무료공부", "고수의", "정보공개", "노하우", "공유방",
        "슈퍼개미", "53만 유투버", "카카오톡", "공개 공부방", "주식", "딥러닝"
    ]

    for phrase in spam_phrases:
        if phrase in message:
            return True

    # Check for suspicious URLs
    urls = re.findall('https?://(?:[-\w.]|(?:%[\da-fA-F]{2}))+', message)
    if urls:
        for url in urls:
            if "me2.kr" in url or "opcn-kakao.com" in url or "han.gl" in url:
                return True

    # Check for unusual number combinations or currency symbols
    unusual_numbers = re.findall(r'\d{2,}', message)
    if unusual_numbers or "원" in message:
        return True

    # If none of the above checks were triggered, classify message as 'not spam'
    return False