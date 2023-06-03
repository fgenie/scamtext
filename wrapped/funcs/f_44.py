def is_spam(message: str) -> bool:
    import re

    # Pattern check for spam keywords
    spam_patterns = [
        "입장번호",
        "투자",
        "상한가",
        "수익",
        "추천",
        "광고",
        "계좌",
        "축하",
        "공개",
        "선물",
        "쿠폰",
        "오픈",
        "무료거부",
        "https?:\/\/",
        "주식",
        "투자반",
        "%"
    ]

    # Check for the presence of spam keywords using regex
    for pattern in spam_patterns:
        if re.search(pattern, message):
            return True

    return False