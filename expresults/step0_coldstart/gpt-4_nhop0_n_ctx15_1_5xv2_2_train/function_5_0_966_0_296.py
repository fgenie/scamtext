
import re

def is_spam(message):
    spam_keywords = [
        'http://', 'https://', '%', '내기', '수익', '추천', '공시', '가즈아', '외환',
        '안전', '보장', '지급', '선물', '무료', '거래', '입장', '금지', '상승', '지원금',
        '투자', '수수료', '폭등', '행복', '안내', '도와', '클릭', '확인', '이벤트', '정회원'
    ]
    
    message_lines = message.split('\n')
    
    # Check for special patterns and overly long messages
    if len(message_lines) > 4 or re.search(r"(.)\1{2,}", message):
        return True

    # Check for keywords in message
    for keyword in spam_keywords:
        if keyword in message.lower():
            return True

    # Check for overly long lines in the message
    for line in message_lines:
        if len(line.split()) > 8 or len(line) > 20:
            return True

    return False
