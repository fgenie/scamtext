
import re

def is_spam(text: str) -> bool:
    # Exclude simple messages
    if len(text.split()) <= 5:
        return False

    # Check for spam keywords
    spam_keywords = ["상한가", "종목", "폭등", "수익", "공개", "오픈초대", "단체방", "vip", "정보", "공유", "Kakao", "확인"]
    for keyword in spam_keywords:
        if keyword in text:
            return True

    # Check for URL patterns
    url_pattern = re.compile(r"http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+")
    urls = url_pattern.findall(text)
    if len(urls) > 0:
        return True

    return False
