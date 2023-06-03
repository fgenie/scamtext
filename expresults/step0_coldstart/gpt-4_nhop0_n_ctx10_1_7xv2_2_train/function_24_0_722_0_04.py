
import re

def is_spam(text: str) -> bool:
    # Rule 1: Detect ads or advertisement keyword
    if re.search(r"(광고)|(\[.?판.?교즘\])", text, re.IGNORECASE):
        return True
    
    # Rule 2: Detect URLs
    if re.search(r"http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*(), ]|(?:%[0-9a-fA-F][0-9a-fA-F]))+", text):
        return True
    
    # Rule 3: Detect specific formats usually found in spam messages
    if re.search(r"([가-힣]* [\d]{2,3} 계약 기준|수량 당 수익 [?,\d]+원|- [2-4]?\d+.% 수익달성)", text):
        return True
    
    # Rule 4: Detect unusual combination of characters or symbols
    if re.search(r"[[:graph:]]+[^\s\w][[:graph:]]+", text):
        return True
    
    # Rule 5: Detect specific keywords usually found in spam messages
    spam_keywords = [
        "지원방", "지원금", "입장코드", "소액투자", "초심자", "상담신청",
        "정보공개", "당첨", "수수료", "공식허가임박", "상한가", "생명공학"
    ]
    for keyword in spam_keywords:
        if keyword in text:
            return True

    return False
