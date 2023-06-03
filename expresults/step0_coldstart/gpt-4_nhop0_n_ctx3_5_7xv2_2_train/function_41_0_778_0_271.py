
import re

def is_spam(message: str) -> bool:
    # Check for common spam patterns such as excessive use of special characters and numbers
    special_chars = re.findall(r'[\W_]', message)
    numbers = re.findall(r'\d', message)
    if len(special_chars) / len(message) > 0.3 or len(numbers) / len(message) > 0.3:
        return True

    # Check for presence of suspicious URL shorteners
    shortener_domains = ["me2.kr", "bit.ly", "tinyurl.com", "goo.gl", "ow.ly", "is.gd"]
    for domain in shortener_domains:
        if domain in message:
            return True

    # Check for typical spam words/phrases
    spam_keywords = ["축하합니다", "테반", "마지막", "창고대방출", "대강당", "균일가전", "할인", "선착순", "특가", "이월상품"]
    for keyword in spam_keywords:
        if keyword in message:
            return True

    # If none of the spam indicators are found, the message is considered normal.
    return False
