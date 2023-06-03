def is_spam(text):
    import re

    # Detect patterns that could be spam
    spam_patterns = [
        r"(?i)님",  # Korean honorific (common in spam messages)
        r"\d주차체험반",  # Korean-style week-specific promotion
        r"(?i)프로모션",  # Promotions
        r"(?i)입장 안내",  # Korean phrase for entering a specific chatroom
        r"(?i)고-배-당",  # High yield/returns (common in financial spam)
        r"(?i)나노 수익",  # Small/tiny profits (common in financial spam)
        r"(?i)정회원방",  # Membership promotions (common in Korean spam)
        r"(?i)선물지급"  # Gift/prize giveaways
    ]

    # Check if any of the spam patterns match the given text
    for pattern in spam_patterns:
        if re.search(pattern, text):
            return True

    # Check for URLs that are likely spam
    spam_url_patterns = [
        r"[^\s]+\.[^\s]+(/[^\s]*)?",
        r"[^\s]+\.com(/[^\s]*)?",
    ]
    for pattern in spam_url_patterns:
        if re.search(pattern, text):
            matched_url = re.search(pattern, text).group(0)
            short_url_domains = ["me2.kr", "kakaotalk.it"]
            for domain in short_url_domains:
                if domain in matched_url:
                    return True

    return False