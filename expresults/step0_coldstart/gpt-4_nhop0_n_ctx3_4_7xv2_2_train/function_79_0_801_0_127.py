
import re

def is_spam(text):
    # Check for presence of typical spam keywords
    spam_keywords = ["상장", "공개", "광고", "소식", "발표", "VIP", "체험", "적선", "참여", "연혁", "거부"]
    for keyword in spam_keywords:
        if keyword in text:
            return True

    # Check for presence of links usually used in spam
    urls = re.findall(r"http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+", text)
    if urls:
        return True
    
    # Check for presence of typical spam phrases
    spam_phrases = ["일주일", "사업 본격화", "무료거부"]
    for phrase in spam_phrases:
        if phrase in text:
            return True

    # Check for excessive number of special characters which might indicate spam
    special_chars = re.findall(r"[^a-zA-Z0-9가-힣 ]", text)
    if len(special_chars) / len(text) > 0.3:
        return True

    # None of the above conditions met, so classify as normal
    return False
