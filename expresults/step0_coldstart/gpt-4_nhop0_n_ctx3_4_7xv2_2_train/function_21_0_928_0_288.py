
import re

def is_spam(message):
    # Check for the use of special characters or unusual repetition of characters
    if re.search(r"[^가-힣a-zA-Z0-9\s,.!?:]", message) or re.search(r"([가-힣a-zA-Z])\1{3,}", message):
        return True

    # Check for the presence of URLs or stock codes
    if re.search(r"https?://\S+|www\.\S+|#[0-9]+|[a-zA-Z]{3,}\([0-9]{6}\)", message):
        return True

    # Check for personal pronouns and common greetings as an indicator of non-spam
    normal_keywords = ["안녕", "하세요", "넵", "감사", "하세요", "가능", "근처", "있나요", "있다"]

    for word in normal_keywords:
        if word in message:
            return False

    return False
