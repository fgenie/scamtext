def is_spam(message):
    import re

    # Check for common spam keywords
    spam_keywords = ["추천", "상승", "공개", "최소", "특허", "대규모투자", "발표", "계열사", "기존", "정보방", "수익", "↑"]

    for keyword in spam_keywords:
        if keyword in message:
            return True

    # Check for URLs with specific format
    url_pattern = re.compile(r'https://me2\.kr/\w{3}')
    urls = url_pattern.findall(message)

    if len(urls) > 0:
        return True

    # Check for excessive use of punctuation
    punctuation_pattern = re.compile(r'[!가-힣]{2,}|[%^&*()@{};:\'\",.><\/\-_=+]{2,}')
    excessive_punctuation = punctuation_pattern.findall(message)

    if len(excessive_punctuation) > 2:
        return True

    return False