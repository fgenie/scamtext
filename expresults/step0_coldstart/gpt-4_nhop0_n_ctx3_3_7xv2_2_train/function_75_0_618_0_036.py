
import re

def is_spam(text):
    spam_keywords = ['무료 상담', '광고', '혜택', '증권', '선물', 'Coin', '부동산', '자산', '수익', '코드', '입장', '행운', '이벤트', '기프티콘', '신규가입']
    normal_keywords = ['하이', '인증번호', '보자']
    
    spam_score = sum([1 for keyword in spam_keywords if keyword in text]) / len(spam_keywords)
    normal_score = sum([1 for keyword in normal_keywords if keyword in text]) / len(normal_keywords)

    if re.search(r'https?://\S+', text) and not any(normal_keyword in text for normal_keyword in normal_keywords):
        return True
    if spam_score > normal_score and spam_score >= 0.5:
        return True
    return False
