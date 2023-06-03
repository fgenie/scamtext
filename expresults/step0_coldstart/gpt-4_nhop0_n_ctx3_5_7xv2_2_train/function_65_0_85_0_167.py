
import re

def is_spam(message):
    spam_keywords = ["http", "https", "www", "배우고", "시작하루", "목표달성", "매집주", "매도", "매수"]

    if len(message.split()) < 6:
        return False
        
    for keyword in spam_keywords:
        if keyword in message:
            return True
            
    if len(re.findall("[!@#$%^&*()_+={}|\\[\]:\";',?/~\-`<>]", message)) >= 2:
        return True

    return False

