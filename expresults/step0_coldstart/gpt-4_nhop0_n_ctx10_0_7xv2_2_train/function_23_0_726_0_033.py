def is_spam(message: str) -> bool:
    import re

    # Define spam keyword patterns
    spam_keywords = [
        r"\b(추천|공개|당첨|최소|종목|지금|실적)[\s\S]*\b(안내|시작|확인|드리|교육|최고|클릭|링크)[\s\S]*\b(등록|무.료|무료|예약|입장|이벤트)\b",
        r"\b(이번|이주|절대|조장|장담|오를때|공시발표|일체비용|현직국회의원|가격|거래량|수익률|운동화|운전자|운전|방역|대출|방번호|원룸|빈방)\b",
        r"(%|)\s*\b(수익|상승|하락|증가|감소|단기간|익절)\b",
        r"(\.at\/|me2\.kr\/|http(s)?:\/\/(www\.)?[-a-zA-Z0-9@:%._\+~#=]{1,256}\.[a-zA-Z0-9()]{1,6}[-a-zA-Z0-9()@:%_\+.~#?&//=]*)",
        r"kakaotalk\.it\/\w+",
        r"님[^\s]+방",
        r"마감시",
        r"업체 드리며"
    ]

    # Check if any spam keyword patterns are found in the message
    for pattern in spam_keywords:
        if re.search(pattern, message):
            return True

    return False