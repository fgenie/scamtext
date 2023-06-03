
import re

def is_spam(message):
    # Check for common spam phrases and patterns
    spam_phrases = [
        r"%\d{1,3}",
        r"급등",
        r"상한가",
        r"최고가",
        r"차별화",
        r"추천",
        r"투자",
        r"차등",
        r"실력",
        r"가입",
        r"새로운",
        r"무료",
        r"거부",
        r"회원",
        r"vip",
        r"서비스",
        r"제공",
        r"고객",
        r"비밀번호",
        r"운영중인",
        r"정부이첩",
    ]
    
    # Check for presence of URLs
    url_pattern = r"http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+"
    urls = re.findall(url_pattern, message, flags=re.IGNORECASE)

    # Check for common spam words in text
    for pattern in spam_phrases:
        if re.search(pattern, message, flags=re.IGNORECASE):
            return True

    # Check if there are more than 2 urls in the message
    if len(urls) > 2:
        return True

    return False
