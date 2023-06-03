import re


def is_spam(message: str) -> bool:
    # Use regex to find URL patterns
    url_pattern = r"(https?://[^\s]+)"
    urls = re.findall(url_pattern, message)

    # If multiple URLs are present in the message, consider it as spam
    if len(urls) > 1:
        return True

    # Check for spam keywords
    spam_keywords = ["단독입수", "체험반", "목표달성기념", "상장스타트업"]
    for keyword in spam_keywords:
        if keyword in message:
            return True

    # If message is in a non-alphanumeric language, consider it as spam
    # (In this case, Korean)
    korean_pattern = r"[\uac00-\ud7a3]+"
    korean_characters = re.findall(korean_pattern, message)
    if len(korean_characters) > 0:
        return True

    # If none of the above conditions are met, the message is not considered spam
    return False