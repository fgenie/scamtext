def is_spam(message: str) -> bool:
    import re

    # Check for URLs
    url_pattern = re.compile(r"http\S+|www\S+|https\S+|me2.kr/\w")
    urls = url_pattern.findall(message)
    if len(urls) > 0:
        return True

    # Check for common spam keywords
    spam_keywords = ["VIP", "체험반", "추천주", "수익", "공시발표", "실력입증"]
    for keyword in spam_keywords:
        if keyword in message:
            return True

    # Check for percentage
    percentage_pattern = re.compile(r"\d{1,3}%")
    percentages = percentage_pattern.findall(message)
    if len(percentages) > 0:
        return True

    # If none of the conditions above are met, the message is considered normal
    return False