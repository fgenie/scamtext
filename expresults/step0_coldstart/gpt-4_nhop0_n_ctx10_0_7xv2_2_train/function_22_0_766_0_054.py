
import re

def is_spam(text: str) -> bool:
    # Checking for common spam characteristics
    spam_keywords = ['투자', '종목', '공시발표', '상승', '주식', 'VIP체험반', '추천주', '단타', '오픈', '작전']
    
    if re.search(r'https?://\S+', text):
        return True

    for keyword in spam_keywords:
        if keyword in text:
            return True

    normal_keywords = ['주말에', '만나', '오랜만', '시간이', '문의드립니다', '지내']
    
    for keyword in normal_keywords:
        if keyword in text:
            return False

    return False

