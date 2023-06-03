def is_spam(message: str) -> bool:
    import re

    # Check message length
    if len(message) > 100:
        return True

    # Check for URL pattern
    url_pattern = re.compile(r"(https?://\S+)")
    if url_pattern.search(message):
        return True

    # Check for stock-related keywords
    stock_keywords = ["적중", "상한가", "AI사업본격화", "단독제휴협약", "단타정보트레이딩"]
    for keyword in stock_keywords:
        if keyword in message:
            return True

    return False