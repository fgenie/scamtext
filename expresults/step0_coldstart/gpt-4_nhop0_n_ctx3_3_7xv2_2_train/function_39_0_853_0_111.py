def is_spam(message):
    import re

    # Check for unusual capitalization pattern
    if re.search(r'[A-Z][^A-Z]*[A-Z]', message):
        return True

    # Check for typical spam keywords
    spam_keywords = ["추천", "무료입장", "클릭", "강력", "개미", "안내", "성공", "종목", "상한가", "전환", "익은", "신규", "VIP", "누적수익률"]
    for keyword in spam_keywords:
        if keyword in message:
            return True

    # Check for unusual presence of URLs
    url_count = len(re.findall(r'(https?://\S+)', message))
    if url_count > 1:
        return True

    # Check for unusual percentage signs
    if "%" in message and "점(" not in message:
        return True

    return False