def is_spam(message: str) -> bool:
    import re

    # Check for common spam keywords
    spam_keywords = ["클릭 종목확인", "주식", "%이상 수익률", "1차목표가", "2차목표가", "3차목표가", "4차목표가", "익 절 가",
                     "정보방에서 상세히 바로 공개됩니다", "누적수익률", "기관 매집", "목표가", "수익률", "주.목", "종.목", "개 무료"]

    for keyword in spam_keywords:
        if keyword in message:
            return True

    # Check for suspicious URLs
    regex_urls = re.compile("https?://(?:[-\w.]|(?:%[\da-fA-F]{2}))+")
    urls = regex_urls.findall(message)
    spam_domain_keywords = ["opcn", "buly"]

    for url in urls:
        for domain_keyword in spam_domain_keywords:
            if domain_keyword in url:
                return True

    # Check for abnormal number of consecutive special characters
    regex_consecutive_special_chars = re.compile("[!@#$%^&*()_+={}|\[\]\\\";:'<>?,\.\/]{3,}")
    consecutive_special_chars = regex_consecutive_special_chars.findall(message)

    if len(consecutive_special_chars) > 0:
        return True

    # Check for abnormal use of percentages
    regex_percentage = re.compile("\d+%")
    percentages = regex_percentage.findall(message)

    if len(percentages) >= 3:
        return True

    # If none of the above conditions were triggered, the message is considered normal
    return False