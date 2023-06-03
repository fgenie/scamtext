
import re

def is_spam(message):
    message = message.lower()
    
    # Check for spam keywords
    spam_keywords = ['카톡방', '목표달성기념', 'orl.kr', 'v.ip방', '바나바나', 'web발신', '광고', '단타매매',
                     '무료거부', '투자반', '할인', '평택에서 부동산', '돼지/소', 'von']
    for keyword in spam_keywords:
        if keyword in message:
            return True

    # Check for URLs with suspicious domains
    urls = re.findall(r'(https?://\S+)', message)
    for url in urls:
        if any(domain in url for domain in ['opcn-kakao.com', 'me2.kr', 'ko.gl', 'vvd.bz']):
            return True

    # Check for unusual characters
    unusual_chars = re.findall(r'\*|▼|▲|^^', message)
    if len(unusual_chars) > 0:
        return True

    # Check for prices and money
    prices = re.findall(r'\d+(?:,?\d+)?원', message)
    if len(prices) > 1:
        return True

    return False
