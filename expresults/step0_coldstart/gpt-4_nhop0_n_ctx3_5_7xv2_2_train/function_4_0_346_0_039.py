def is_spam(message: str) -> bool:
    import re
    
    # Check for short links
    short_links = re.findall(r'(http(s)?:\/\/\S*?\.(\S{2,3}|\w{2}))(?=([\s\b]|[.,!?\n]|$))', message)
    if short_links:
        return True

    # Check for high percentage words
    high_percentage_words = re.findall(r'(\d{2,3}[%])', message)
    if high_percentage_words:
        return True

    # Check for keywords indicating spam
    spam_keywords = ["당일 출금가능", "추천주", "예상하는 쉬운투자", "이동", "적중", "돌파", "다음주 종목도 이어서 오픈합니다", "나갑니다"]
    for keyword in spam_keywords:
        if keyword in message:
            return True

    # If none of the above conditions are met, the message is not spam
    return False