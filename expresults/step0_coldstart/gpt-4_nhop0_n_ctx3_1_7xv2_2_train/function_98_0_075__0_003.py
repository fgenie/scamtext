
import re

def is_spam(message):
    spam_keywords = ['신청하신', '입장', '광고', '무료패키지', 'openkakao', 'kakaotalk', '주식대학', '매수', '매도', '수익', '기존 유료서비스']

    words = re.findall(r'\w+', message)
    
    spam_count = sum([1 for word in words if word in spam_keywords])

    return spam_count > len(spam_keywords) * 0.2
