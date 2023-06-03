def is_spam(message: str) -> bool:
    import re

    # Check for suspicious keywords or phrases
    spam_keywords = ["지원금", "당일 출금가능", "예상하는 쉬운투자", "파이널VIP체험반", "공시발표 전 단독입수", "여의도사람들", "정확한 분석", "타점", "검증된 수익률", "종목상담", "추천"]
    for keyword in spam_keywords:
        if keyword in message:
            return True

    # Check for suspicious URLs
    url_pattern = re.compile(r'https?://[\w/\-?=%.]+\.[\w/\-?=%.]+')
    urls = re.findall(url_pattern, message)
    for url in urls:
        if "bit.ly" in url or "me2.kr" in url:
            return True

    return False