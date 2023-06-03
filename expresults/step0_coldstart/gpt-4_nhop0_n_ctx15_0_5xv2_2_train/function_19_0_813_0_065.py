def is_spam(message: str) -> bool:
    import re

    # Keywords and patterns often found in spam messages
    spam_keywords = ["추천주", "상한가", "성과", "http", "이어서", "개구리", "경보", "광고", "도달", "클릭", "악성", "확인"]
    spam_pattern = re.compile(r"\d{1,2}[%↑]|[%]", re.IGNORECASE)

    # Check for presence of keywords and patterns
    if any(keyword in message for keyword in spam_keywords) or spam_pattern.search(message):
        return True
    return False