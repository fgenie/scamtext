
import re

def is_spam(message: str) -> bool:
    # Check for url shorteners or suspicious keywords in the message
    url_shorteners = ["bit.ly", "me2.kr", "ko.gl", "openkakao.at", "mpp23.com"]
    spam_keywords = ["증권", "매집주", "공개", "입장", "종목추천", "카카오톡", "출금", "혜택", "실력보셨죠?", "상승", "특허임박", "공시", "파이널VIP", "투자"]
    
    # Check if message contains any url shortener
    for url_shortener in url_shorteners:
        if url_shortener in message:
            return True

    # Check if message contains any spam keyword
    for keyword in spam_keywords:
        if keyword in message:
            return True
    
    # Check for number patterns (e.g. 11일 추천 수익 축하합니다)
    number_patterns = re.findall(r'\d{1,2}일', message)
    if len(number_patterns) > 0:
        return True

    return False
