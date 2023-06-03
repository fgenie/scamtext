import re

def is_spam(text):
    spam_indicators = [
        r'\b추천',
        r'\b\d{2,4}%',
        r'\b광고\b',
        r'\b(상승|익절)',
        r'\bhttps?:\/\/\S*',
        r'\b(실력입증|스윙 매매)',
        r'KEY:',
        r'\b무료추천주',
        r'\b(안전하고 확률 높은)',
        r'\b(수익 보장)',
        r'\브[이|벳]트\w',
        r'\b(파이널VIP체험반)',
        r'\b(지급|오픈)',
        r'\b(\d{1,2}월|간편)+',
        r'\bbit.ly',
    ]
    
    normal_indicators = [
        r'\b배달 기사입니다\b',
        r'\b(오랜만이다|잘 지내냐|밥 먹었냐|하루에 평균)',
        r'(키움증권|키움금융센터)',
        r'(주식|주식수수료율)',
        r'(SMS수신설정방법|무료수신거부|준법감시인 심사필)',
    ]

    if any(re.search(pattern, text) for pattern in normal_indicators):
        return False

    if any(re.search(pattern, text) for pattern in spam_indicators):
        return True

    return False