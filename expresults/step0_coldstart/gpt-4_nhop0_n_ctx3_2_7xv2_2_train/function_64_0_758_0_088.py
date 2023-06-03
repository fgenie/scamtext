
import re

def is_spam(message):
    # Rule 1: Check for spam keywords
    spam_keywords = ['축하합니다', '힘든시기', '당첨', 'vvd.bz', '광고', '무료방매수사인', 'bit.ly', '성착', '무료거부', '정부기관 관련', 'me2.kr']
    for keyword in spam_keywords:
        if keyword in message:
            return True

    # Rule 2: Check for excessive use of numbers and special characters
    numbers = len(re.findall(r'\d+', message))
    special_chars = len(re.findall(r'[^a-zA-Z0-9가-힣\s\w]', message))
    if numbers > 5 or special_chars > 10:
        return True

    # Rule 3: Check for URLs that are not from reputable sources
    bad_urls = ['vvd.bz', 'bit.ly', 'me2.kr']
    for url in bad_urls:
        if url in message:
            return True

    return False
