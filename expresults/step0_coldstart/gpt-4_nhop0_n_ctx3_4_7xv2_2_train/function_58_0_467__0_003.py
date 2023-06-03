
import re

def is_spam(text):
    spam_keywords = ['무 료 체 험', '자 동 매 매', '고-배-당', '선물지급', '프로모션', '알려드린']
    url_pattern = r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+'
    urls = re.findall(url_pattern, text)
    
    for keyword in spam_keywords:
        if keyword in text:
            return True
            
    if urls:
        spam_url_ratio = sum([bool(re.search(r"ko\.gl|me2\.kr|click\s*here", url)) for url in urls]) / len(urls)
        if spam_url_ratio > 0.5:
            return True

    return False
