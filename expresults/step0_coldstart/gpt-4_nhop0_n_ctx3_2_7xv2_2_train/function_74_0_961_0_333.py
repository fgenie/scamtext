def is_spam(text: str) -> bool:
    import re

    # Check for unusual patterns, multiple urls and consecutive caps lock usage
    unusual_pattern = re.compile(r"[^가-힣-\n\.,!\?'\[\]\(\)\{\}: ][\n]*")
    urls = re.findall(r"http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\\(\\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+", text)
    consecutive_caps = re.findall(r"([A-ZÀ-ÿ\u0100-\u017F]\s*){3,}", text)

    # Check for specific keywords related to spam messages
    spam_keywords = ['축하', '당첨', '목표가', '단독 정보', '무료입장', '알짜 종목']

    if len(urls) > 1 or len(consecutive_caps) > 1 or unusual_pattern.search(text):
        return True

    for keyword in spam_keywords:
        if keyword in text:
            return True

    return False