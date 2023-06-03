def is_spam(message):
    import re

    # Check for common spam keywords and phrases
    spam_keywords = ["축하합니다", "4월체험반", "최소", "상승", "상한가", "폭등", "익절", "외수익", "적은시간 만에", "손실 없습니다",
                     "무료거부", "무료입장", "광고", "신청", "혜택", "해으십시오", "강요드리지 않습니다", "주식은 오를때", "카카오톡제재",
                     "텔레그램", "악성광고", "입장 안내", "서비스 가입", "이벤트", "로보마켓", "알려드린", "상한가달성"]

    # Check for multiple URL patterns in the message
    url_patterns = [r"http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+",
                    r"me2[\w.]+",
                    r"han.gl[\w./]+",
                    r"kakao[\w.]+",
                    r"asq.kr[\w./]+",
                    r"[a-zA-Z]+://[\S]+"]

    for keyword in spam_keywords:
        if keyword in message:
            return True

    for pattern in url_patterns:
        match = re.search(pattern, message)
        if match:
            return True

    return False