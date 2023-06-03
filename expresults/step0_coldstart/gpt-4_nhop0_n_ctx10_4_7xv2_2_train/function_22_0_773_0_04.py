
import re

def is_spam(message):
    message = message.lower()
    
    spam_keywords = [
        "광고", "무료수신거부", "증시", "선물", "매수", "매도", "목표가", "종목", "투자",
        "최고급", "오픈초대", "회원", "상승", "폭등", "거래량", "지금 가격", "이벤트"
    ]

    link_patterns = [
        r"http[s]{0,1}:\/\/[-_A-Za-z0-9.\/=?%&]+",
        r"[-_A-Za-z0-9.\/]+[\._\/|]{1}[-_A-Za-z0-9&=%?\/]+",
        r'kakaotalk\.at\/[-_A-Za-z0-9]+',
        r'me2\.[-_A-Za-z0-9.]*\/[-_A-Za-z0-9]+'
    ]

    spam_counter = 0
    
    # Check for spam keywords
    for keyword in spam_keywords:
        if keyword in message:
            spam_counter += 1
            
    # Check for spam URLs
    for pattern in link_patterns:
        if re.search(pattern, message):
            spam_counter += 1

    return spam_counter >= 2

