
import re

def is_spam(message: str) -> bool:
    # Checking for spam URL patterns
    spam_url_patterns = [
        r"(?i)https?:\/\/(?:me2\.kr|buly\.kr|opcn\-kakao.com|han.gl|abit\.ly)/\S*",
        r"(?i)ⓢlⓩ102\.com",
        r"(?i)orl\.kr\/\S*",
        r"(?i)https?://openkakao.io/\S*"
    ]

    for pattern in spam_url_patterns:
        if re.search(pattern, message):
            return True

    # Checking for other spam patterns
    spam_patterns = [
        r"(?i)(vip|vvip)투자반",
        r"(?i)차별화 된",
        r"(?i)시작하루만에",
        r"(?i)추천주 현황",
        r"(?i)slot🎰zone",
        r"(?i)지니틱스",
        r"(?i)카카오톡제재",
        r"(?i)[5일평균].*[8,930.000원]",
        r"(?i)문의▼",
    ]

    for pattern in spam_patterns:
        if re.search(pattern, message):
            return True

    # If none of the spam patterns are present
    return False
