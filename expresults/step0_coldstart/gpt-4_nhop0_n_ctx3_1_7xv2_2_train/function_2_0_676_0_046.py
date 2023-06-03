
import re

def is_spam(text):
    # Checking for signs of spam
    spam_keywords = [
        '적중', '상승확정', '익절', '폭등 예상', '올라갑니다',
        '무조건 올라갑니다', '상한가달성', '단기간에',
        '수익', 'http', '://', 'https', '://',
        'openkakao', '.it', 'opcn-kakao', '.com',
        '잠정', '입장하셔서',
        ]
    count = 0
    for keyword in spam_keywords:
        count += len(re.findall(keyword, text))
    
    # Return True if spam indicators are present
    if count > 2:
        return True
    else:
        return False
