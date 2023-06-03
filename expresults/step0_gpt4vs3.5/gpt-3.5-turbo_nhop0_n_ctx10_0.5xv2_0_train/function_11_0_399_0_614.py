
import re

def is_spam(text):
    # lower case the text
    text = text.lower()
    
    # remove all urls
    text = re.sub(r'http\S+', '', text)

    # check for spam keywords
    spam_keywords = ['카톡방', 'openkakao', '주 2,720,000원 성공', '무료체험', '승인전화X', 
                     '미미', '매10%', 'BBQ', 'asd700', 'abit.ly', '3일 연속 VI 적중',
                     '급등예정 종목', '구 유벳', '계좌 작업', 'AP 입금', '출금한도', '어질러져']
    for keyword in spam_keywords:
        if keyword in text:
            return True
    
    # check number of digits ratio
    digits_count = sum(c.isdigit() for c in text)
    letters_count = sum(c.isalpha() for c in text)
    digits_ratio = digits_count / max(letters_count, 1)
    if digits_ratio > 0.2:
        return True
    
    # check length
    if len(text) < 15:
        return True

    # otherwise, it's normal text
    return False
