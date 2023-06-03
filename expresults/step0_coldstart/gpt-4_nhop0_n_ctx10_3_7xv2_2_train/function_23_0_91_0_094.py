
import re

def is_spam(text):
    # Check for unusual symbols or patterns
    unusual_patterns = ["ＢTP-7942.COM", "콛、SK77", "쳣20,먜10", "https://me2.kr", "https://bit.ly", "https://kakaotalk.it"]
    for pattern in unusual_patterns:
        if pattern in text:
            return True

    # Check for excessive use of special characters or numbers
    if len(re.findall(r'[^a-zA-Z가-힣\s.,?!]', text)) > 5 or len(re.findall(r'\d', text)) > 4:
        return True

    # Check for specific spam keywords
    spam_keywords = ["공시발표", "무료참여", "해선", "체험반", "드리며 시작", "성취", "주식추천", "리뉴얼", "선물거래", "투자 가이드", "손해없는해외식", "투자호회", "특별혜택", "등 빵빵한 지원", "입장만 해도 커피 기프티콘", "행복해지자"]
    for keyword in spam_keywords:
        if keyword in text:
            return True

    # Check for excessive use of white spaces or line breaks
    if len(re.findall(r'\s\s+', text)) > 1 or len(re.findall(r'\n\n+', text)) > 1:
        return True

    return False
