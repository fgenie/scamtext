def is_spam(message: str) -> bool:
    import re

    # Heuristics & Regular Expressions for detecting spam
    patterns = [
        r"(\d+%\s?[↑ 적중])",  # Percentage increase/decrease
        r"(목표달성기념|추천주|급등예정|실력입증|실력보셨죠?|체험반|vip체험반|일타강사진)",  # Likely spam keywords
        r"(\d+만원|처음혜택|다음주 종목)",  # Monetary gains
        r"([(]?광고[)]?)",  # Advertising keyword
        r"(카카오톡?[.]\w+)",  # Typical spam domains
        r"(https://(me2\.kr|han\.gl)/\w+)",  # Common spam URLs
        r"(비밀번호[\s:]*(\d{4}))"  # Confidential information
    ]

    for pattern in patterns:
        if re.search(pattern, message):
            return True
    return False