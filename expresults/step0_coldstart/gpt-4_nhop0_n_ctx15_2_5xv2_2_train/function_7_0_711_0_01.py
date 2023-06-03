def is_spam(message: str) -> bool:
    import re
    
    # Patterns for detecting spam
    patterns = [
        r"(?i)\b(추천|상승|단기간|익절|무료교육|달성|거래량|폭등)\b", # 유형 1,2,4에서 발견됩니다.
        r"(?i)\b(http|bit\.ly|t\.ly|me2\.kr|dokdo\.in|buly\.kr)\b", # 유형 1,2,3,4,5에서 발견됩니다.
        r"(?i)\b(입금|출금)\b", # 일부 스팸 메시지에서 발견됩니다.
        r"(%|상한가|모션|목표)\b", # 일부 스팸 메시지에서 발견됩니다.
        r"(?i)\b(광고)\b", # 스팸 메시지에서 때때로 발견됩니다.
    ]
    
    for pattern in patterns:
        if re.search(pattern, message):
            return True
    
    return False