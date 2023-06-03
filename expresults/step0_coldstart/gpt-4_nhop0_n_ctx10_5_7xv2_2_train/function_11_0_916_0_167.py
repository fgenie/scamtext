
import re

def is_spam(message):
    spam_keywords = ['(광고)', '추천주', '상한가', '무료거부', '거래소', '알뜰폰', '선물', '주식', '주가', '수익', '결제', '늘은 확실', '경상도', '프로젝트', '최소인원으로', '실력입증', '무료로 참여', '무상']
    message_split = re.split(r'\W+', message.lower())
    for keyword in spam_keywords:
        if keyword.lower() in message_split:
            return True

    spam_phrases = [r'https?://(?:[-\w.]|(?:%[\da-fA-F]{2}))+', r'\d+\w*%*']
    for phrase in spam_phrases:
        if re.search(phrase, message):
            return True

    return False
