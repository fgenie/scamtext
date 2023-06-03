
import re

def is_spam(message: str) -> bool:
    # Check for typical spam keywords/phrases
    keywords = ["추천", "입장", "알려드린", "참여", "상승", "적중", "상한가", "투자", "만들기", "마지막안내", "오픈합니다", "다음주", "계약", "이벤트", "광고"]
    
    for keyword in keywords:
        if keyword in message:
            return True
    
    # Check for multiple consecutive special characters (excluding Korean)
    if re.search("[^\w\sㄱ-ㅣ가-힣]+[^\w\sㄱ-ㅣ가-힣]+", message):
        return True
    
    # Check for excessive capitalization
    if sum(1 for c in message if c.isupper()) > len(message) / 2:
        return True
    
    # Check for links with suspicious domains
    spam_domains = ["me2.kr", "han.gl", "ko.gl", "vvd.bz"]
    for domain in spam_domains:
        if domain in message:
            return True

    return False
