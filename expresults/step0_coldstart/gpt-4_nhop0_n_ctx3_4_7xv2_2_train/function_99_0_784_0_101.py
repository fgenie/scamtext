
import re

def is_spam(message):
    # Regular expressions to detect spam patterns
    spam_patterns = [
        r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}",
        r"(?P<url>https?://[^\s]+)",
        r"\u200b",
        r"금전요구",
        r"(비밀번호|코드|URL|URL 도메인|지원금|상품권|커피):( *)?[0-9A-Za-z가-힣]*",
        r"\[.{1,20}\]",
        r"\d{1,10}(,| |, |)\d{1,10}(,| |, |)\d{1,10}(,| |, |)\d{1,10}",
        r"(구매|혜택|이벤트|확인)을(.|은)?(\s)?(없|아니|습니까|우세요)",
    ]
    
    for pattern in spam_patterns:
        if re.search(pattern, message):
            return True
    
    return False
