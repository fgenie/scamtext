def is_spam(text):
    import re

    spam_indicators = [
        r'https?:\/\/(me2\.kr|link\.jeongyookgak\.com|vvd\.bz|buly\.kr|opcn-kakao\.com)',
        r' \% \^ \↑',
        r'\%\d',
        r'\d{1,2}\,\d{3}',
        r'[0-9]\,[0-9]{1,2}0 원',
        r'0\.[0-9]{5}',
        r'[0-9]{1,3}\%\↑',
        r'(신규|다음주|전문가|택배|시작|무료|세력|목표가)[\.\,\!\?]',
        r'(발표|익절|이벤트|정보|입수|작전|합류)',
        r'[0-9]{1,2}일 추천주',
    ]

    if any(re.search(indicator, text) for indicator in spam_indicators):
        return True
    else:
        return False