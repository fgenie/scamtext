
import re

def is_spam(message):
    message = message.lower()
    spam_keywords = [
        "bit.ly", "tinyurl.com", "awe.sm", "goo.gl", "me2.kr", "ocx.kr", "kakaotalk.at", "naver.me", "openkakao.it",
        "대형그룹의 투자", "암호화폐", "상장기업", "총 수익", "성과인증", "지적재산권",
        "집중 추천", "추천주", "주식", "수익", "상승", "적중", "무료체험반", "단타거래",
        "지원금", "특허", "타이밍", "M&A", "창고식", "매매", "관망", "매수"]

    for keyword in spam_keywords:
        if keyword in message.lower():
            return True
    if 'https://' in message or 'http://' in message:  # Check if message contains link
        urls = re.findall('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\\(\\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', message)
        for url in urls:
            # Check if url contains any scam/spam keywords
            if not set(url.split('/')).isdisjoint(spam_keywords):
                return True
    return False
