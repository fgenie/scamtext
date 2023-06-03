
import re

def is_spam(message):
    spam_keywords = [
        r'\b(?:성과|적중|\d{1,2}\.\d+%|무료거부|확인해보세요|자본지원금)',
        r'\b(?:http|https)://',
        r'\b(?:bit\.ly|me2\.kr)',
        r'(주)[^\s]*(NFT|운용)',
        r'(골동품|명품시계|고급와인) 조각구매'
    ]
    
    for keyword in spam_keywords:
        if re.search(keyword, message, re.IGNORECASE):
            return True
    return False
