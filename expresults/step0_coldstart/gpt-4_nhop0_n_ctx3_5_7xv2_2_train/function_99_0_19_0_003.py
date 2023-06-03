
import re

def is_spam(message: str) -> bool:
    # Check if message contains common spam phrases or keywords
    spam_phrases = ['무료방매수사인', '텔레그램으로 이동', '최고급 정보', '선착', '무료거부', '악성광고', '카카오톡제재', '거래량 폭등 확정']
    for phrase in spam_phrases:
        if phrase in message:
            return True

    # Check if message contains unusual amount of url shorteners or suspicious urls
    url_shorteners = ['bit.ly', 'me2.kr', 'openkakao.at']
    suspicious_url_count = 0
    for url in url_shorteners:
        suspicious_url_count += message.count(url)
        if suspicious_url_count > 1:
            return True

    # Check if message is dominated by numbers
    numbers_count = len(re.findall(r'\d+', message))
    message_length = len(message)
    
    number_ratio = numbers_count / message_length
    if number_ratio > 0.2:
        return True

    return False
