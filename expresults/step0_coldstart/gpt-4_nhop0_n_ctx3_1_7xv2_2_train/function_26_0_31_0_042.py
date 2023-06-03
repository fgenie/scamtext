def is_spam(message: str) -> bool:
    import re

    # Check for spam keywords
    keywords = ["광고", "지급.kr", "입장코드", "30만원", "수익", "소액투자", "선물투자", "지원금", "수수료", "월 최대", "지인추천", "무한", "무료 모의투자", "안정적인 HTS", "자동으로 편리하게", "월 천 고정수입"]
    
    regex = "|".join(keywords)
    if re.search(regex, message):
        return True

    # Check for too many exclamation marks or question marks
    if len(re.findall(r'!', message)) > 3 or len(re.findall(r'\?', message)) > 3:
        return True

    # Check for urls
    url_pattern = re.compile(r'(https?://\S+)')
    urls = url_pattern.findall(message)

    for url in urls:
        if re.search("ko.gl|buly.kr", url):
            return True

    return False