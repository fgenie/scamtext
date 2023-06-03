
import re

def is_spam(message: str) -> bool:
    spam_keywords = ["광고", "축하", "참여", "정보", "비밀", "발표", "상한가", "체험반", "수익", "적중", "지금 사전등록하고 무료관람하세요."]
    check_message = message.lower()
    
    if re.search(r"http\S+", check_message) or re.search(r"www\.\S+", check_message):
        return True

    for keyword in spam_keywords:
        if keyword in check_message:
            return True
        
    return False
