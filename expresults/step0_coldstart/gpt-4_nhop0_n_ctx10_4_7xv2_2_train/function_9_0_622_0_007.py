
import re

def is_spam(text):
    # Check for typical spam words and phrases
    spam_indicators = [
        "VIP", "비밀번호", "상한가", "공시정보", "수익률", "종목상담", "추천", "구유벳",
        "체험반", "안전하고 확률 높은", "추천주 현황", "채팅방종료안내", "목표달성기념",
        "오픈합니다", "공개합니다", "참여", "적중", "검증된", "체험", "실력보셨죠"]
    
    for indicator in spam_indicators:
        if indicator in text:
            return True

    # Check for typical spam URLs
    url_pattern = re.compile(r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\\(\\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+')
    urls = re.findall(url_pattern, text)
    
    for url in urls:
        url_shortener_domains = ["me2.kr"]
        for domain in url_shortener_domains:
            if domain in url:
                return True

    return False
