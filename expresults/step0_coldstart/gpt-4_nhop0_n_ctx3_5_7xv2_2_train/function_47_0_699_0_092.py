
import re

def is_spam(message: str) -> bool:
    # Check for typical spam words/phrases in message
    spam_words = ["추천주", "상담하기", "참여", "실력입증", "성투1등", "VIP", "상한가", "MOU", "체험반", "목표달성기념", "디젠스", "연혁"]

    for word in spam_words:
        if word in message:
            return True

    # Check for URL shorteners which are common in spam messages
    domain_shorteners = ["vo.la", "me2.kr"]
    for domain in domain_shorteners:
        if domain in message:
            return True

    # Check for multiple uppercase letters and special characters
    if len(re.findall(r'[A-Z]', message)) > 5 or len(re.findall(r'[!@#$%^&*()_+]', message)) > 5:
        return True

    # If none of the above conditions are met, message is assumed normal
    return False
