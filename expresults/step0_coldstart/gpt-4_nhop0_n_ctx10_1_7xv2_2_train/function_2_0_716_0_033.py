
import re

def is_spam(message):
    spam_keywords = ["(광고)", "추천주", "기업명", "비밀번호", "정부", "코드", "코인", "종목상담", "종목추천"]
    message = message.lower()

    if any(re.search(keyword.lower(), message) for keyword in spam_keywords):
        return True

    urls = re.findall(r"http[s]?://(?:[a-z0-9]|[.-]|[!*\(\),]|(?:%[0-9a-fa-f][0-z9a-fa-f]))+", message)
    
    if len(urls) > 0:
        return True
    return False
