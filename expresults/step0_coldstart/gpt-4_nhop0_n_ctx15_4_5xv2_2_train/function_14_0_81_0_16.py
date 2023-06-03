import re

def is_spam(message):
    # Check for common spam keywords and phrases
    spam_keywords = ['(광고)', '폭등', '상승', '수익', '마감', '종료', '공시', '이벤트', '오픈초대', '공개하겠습니다', '무료건', '이상상승', '최대', '할인', '보상', '단기수익', 'VIP', 'https://', 'http://']
    for keyword in spam_keywords:
        if keyword in message:
            return True

    # Check for excessive use of special characters
    special_chars = re.findall('[^a-zA-Z0-9가-힣\s]', message)
    if len(special_chars) / float(len(message)) > 0.2:
        return True

    # Check for excessive use of numbers
    numbers = re.findall(r'\d+', message)
    if len(numbers) / float(len(message)) > 0.2:
        return True

    # Check for excessive use of capital letters
    capital_letters = re.findall('[A-Z]', message)
    if len(capital_letters) / float(len(message)) > 0.2:
        return True

    return False