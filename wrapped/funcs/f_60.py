def is_spam(message: str) -> bool:
    import re
    
    # Check for money-related words or symbols
    money_keywords = ["원", "수익", "이익", "상승", "월공개", "현황", "롤", "지원금", "현황", "추천주", "대박", "지갑", "출금", "추천", "경제", "경제야", "하락", "주식", "주가", "수익률", "분기", "최근", "금전요구", "매매", "최고의", "장점", "event", "code", "일물천금", "%", "회원가입", "광고", "연이은", "숫자를", "총 수익", "▼", "▲", "(광고)", "오키"]

    # Check for URL patterns
    url_pattern = re.compile(r'https?://\S+|www\.\S+')
    
    # Check for message length
    if len(message) > 100:
        return True
    
    # Check for unusual repetitions in the message
    repeated_pattern = re.compile(r'(\b\w+\b)(.*\1){3,}.*')
    if repeated_pattern.search(message):
        return True

    # Check for money-related words
    if any(keyword in message for keyword in money_keywords):
        return True

    # Check for URLs in the message
    if url_pattern.search(message):
        return True

    return False