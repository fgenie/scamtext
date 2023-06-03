
import re

def is_spam(text):
    spam_keywords = ["광고", "무료수신거부", "%", "수익", "달성", "단타",
                     "안내", "신청", "컨설팅", "최고급", "세력", "증권", "투자",
                     "거래량", "이익", "수익률", "상승", "폭등", "상한가",
                     "최대", "할인", "특가", "판매", "주식"]

    text = text.lower()
    tokens = re.split(r'\s+|[,.!?]', text)
    
    spam_count = 0
    for keyword in spam_keywords:
        spam_count += tokens.count(keyword)
    
    return spam_count >= 2

