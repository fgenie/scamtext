def is_spam(message: str) -> bool:
    import re
    from collections import Counter

    # Check for excessive use of characters or symbols typically found in spam messages
    def excessive_characters(text: str, threshold: float = 0.2) -> bool:
        common_spam_characters = "!%$*#_<>"

        count = 0
        for char in common_spam_characters:
            count += text.count(char)

        return count / len(text) >= threshold

    # Check for high percentage of uppercase letters in the message
    def excessively_uppercase(text: str, threshold: float = 0.6) -> bool:
        uppercase_count = sum(1 for char in text if char.isupper())
        return uppercase_count / len(text) >= threshold

    # Check for the presence of spam keywords in the message
    def spam_keywords(text: str) -> bool:
        keywords = ["상승", "수익", "VIP", "주식", "추천종목", "근거", "리딩방", "카톡", "새로운 종목", "차트"]

        for keyword in keywords:
            if keyword in text:
                return True
        return False

    # Check for any suspicious URLs
    def suspicious_urls(text: str) -> bool:
        url_pattern = re.compile(r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\\(\\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+')
        urls = url_pattern.findall(text)

        suspicious_domains = ["me2.kr", "vvd.bz", "openkakao", "opcn-kakao"]

        for url in urls:
            for domain in suspicious_domains:
                if domain in url:
                    return True
        return False

    # Clean the message text
    message = re.sub(r'\n', '', message)

    if excessive_characters(message) or excessively_uppercase(message) or spam_keywords(message) or suspicious_urls(message):
        return True
    else:
        return False