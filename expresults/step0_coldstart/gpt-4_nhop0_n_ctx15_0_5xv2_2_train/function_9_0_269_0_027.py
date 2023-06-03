
import re

def is_spam(message: str) -> bool:
    spam_keywords = ["주식", "수익", "상승률", "탈모", "첫20%", "무료거부", "최대 할인", "초록", "용성"]
    urls_regex = r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+'
    excessive_special_chars = r'(\*\*\*|\$\$\$|\?\?\?|!!|▶|\/\/\/|%%%|^https://|^http://)'
    excessive_url_count = len(re.findall(urls_regex, message)) > 2

    for keyword in spam_keywords:
        if keyword in message:
            return True
    
    if re.search(excessive_special_chars, message) or excessive_url_count:
        return True
    
    return False
