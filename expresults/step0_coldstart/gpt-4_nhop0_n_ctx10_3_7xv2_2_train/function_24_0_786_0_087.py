def is_spam(message):
    import re
    
    spam_keywords = ["VIP체험반", "https://me2.kr", "웃음이 넘치는 행복의 길", "70,000P 무료",
                     "목표달성기념", "수익 축하", "안녕하세요 부족함이 없는", "무료거부"]
    for keyword in spam_keywords:
        if keyword in message:
            return True
    
    if re.search(r"\d{3,}", message):
        return True

    if re.search(r"\d{1,2}월체험", message):
        return True

    if re.search(r"\d{1,2}일 알려드린", message):
        return True

    return False