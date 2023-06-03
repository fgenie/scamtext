def is_spam(message):
    import re
    
    spam_keywords = ["적중", "단독입수", "목표달성기념", "추천", "파이널VIP체험반"]
    short_url_pattern = r"(https?:\/\/me2\.kr\/\w+)"

    if any(keyword in message for keyword in spam_keywords):
        return True

    if re.search(short_url_pattern, message):
        return True

    return False