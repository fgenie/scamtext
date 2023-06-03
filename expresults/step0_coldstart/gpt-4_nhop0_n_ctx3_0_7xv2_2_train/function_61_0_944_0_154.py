
import re

def is_spam(message):
    # Check for typical spam words and patterns
    spam_words = ["비결", "하루", "최고급", "설치", "가능", "신익수", "무료", "상담", "추천", "매수", "상한가", "수익률", "이벤트"]
    for word in spam_words:
        if word.lower() in message.lower():
            return True

    # Check for url shortening services
    url_shortening_services = ["bit.ly", "me2.kr", "openkakao.it"]
    for service in url_shortening_services:
        if service.lower() in message.lower():
            return True

    # Check for excessive use of special characters and numbers
    if sum(c.isdigit() or c in ["%", "↑", "↓", "+", "!"] for c in message) > 5:
        return True

    # Check for large white spaces between words
    if len(re.findall('\s{2,}', message)) > 1:
        return True

    # Check for messages containing both English and Korean
    if re.search('[a-zA-Z]', message) and re.search('[가-힣]', message):
        return True

    return False
