def is_spam(message):
    import re

    # Check for presence of spam keywords and phrases
    spam_keywords = ["축하합니다", "상한가", "단독제휴협약", "목표달성기념", "추천", "\d+[월|일]체험반"]
    spam_keyphrase_patterns = [re.compile(keyword) for keyword in spam_keywords]
    
    for pattern in spam_keyphrase_patterns:
        if pattern.search(message):
            return True

    # Check for the presence of suspicious URLs
    url_pattern = re.compile("https://me2.kr/\w+")
    if url_pattern.findall(message):
        return True

    return False