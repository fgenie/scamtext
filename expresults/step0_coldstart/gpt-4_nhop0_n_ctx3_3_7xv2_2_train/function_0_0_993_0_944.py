
import re

def is_spam(message):
    # Check for common spam keywords
    keywords = [
        "무료", "광고", "주식", "대출", "실현", "수익", "월 천", " 종목", "확장", " 현직국 회의원",
        "공개", "폭등", "월급", "정원 만료", "입장", "매수", "매도", "알에프세미", "지아이텍", "경동인베스트",
        " 상한가달성", "하이딥", " 경제", " 정보", "상승", "출구 전략"
    ]
    for keyword in keywords:
        if keyword in message:
            return True

    # Check for presence of URLs
    urls = re.findall(r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', message)
    if len(urls) > 0:
        return True

    # Check for repeated sentences or phrases
    phrases = re.findall(r'([^.!?]*(?:([^.!?]+)[^.!?]*){2})', message)
    if len(phrases) > 0:
        return True

    return False
