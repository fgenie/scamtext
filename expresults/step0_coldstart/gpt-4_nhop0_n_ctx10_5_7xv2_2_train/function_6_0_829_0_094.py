
import re

def is_spam(message):
    # Check for spammy words or phrases
    spam_keywords = ["축하합니다", "광고", "무료수신거부", "지원합니다", "적중", "혜택", "추천주", "투자계획", "수익", "지원금", "특별 할인", "경제야 놀자", "빚에서 벗어", "월 최대", "안전하게 시작하세요", "무료거부", "특별한 혜택", "단독입수한 종목", "급등예정 종목"]

    for keyword in spam_keywords:
        if keyword in message:
            return True
    
    # Check for short URLs
    url_regex = re.compile(r'(?:http|ftp|https)://(?:[\w_-]+(?:(?:\.[\w_-]+)+))(?:[\w.,@?^=%&:/~+#-]*[\w@?^=%&/~+#-])?')
    urls = url_regex.findall(message)
    
    if urls:
        for url in urls:
            if "bit.ly" in url or "me2.kr" in url or "vvd.bz" in url or "han.gl" in url or "yotqt.com" in url:
                return True

    # Check for message length
    if len(message) > 300:
        return True

    # Check for excessive use of special characters
    special_characters_count = sum([message.count(c) for c in '!@#$%^&*()-=_+[]{}|;:,.<>?/'])
    if special_characters_count > 5:
        return True

    return False
