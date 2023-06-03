def is_spam(message: str) -> bool:
    import re
    
    # Regular expressions to detect spam characteristics
    spam_url_pattern = re.compile(r"(https?://){0,1}(me2\.kr|mp{2}\d{2,}|광고|M(\d{1,2})\w{1,}|openkakao\.at)", re.IGNORECASE)
    pattern_percentage = re.compile(r"\d{1,3}%")
    pattern_numbers = re.compile(r"\d{4,}")
    pattern_ad = re.compile(r"\(광고\)", re.IGNORECASE)
    pattern_month = re.compile(r"[M123456789]\W{0,3}[월]", re.IGNORECASE)
    pattern_vip = re.compile(r"vip", re.IGNORECASE)
    pattern_stock = re.compile(r"(추천주|종목|증권|매수세|기관|상한가|정확한 분석|검증된 수익률|알에프세미|지아이텍|광무|와이투솔루션|경동인베스트|하이딥|조선알미늄|에스비비테크|케이사인|더메티팜)(?!.*계약)->"
                             , re.IGNORECASE)
    
    # Checking for spam patterns in the message
    if spam_url_pattern.search(message):
        return True
    if pattern_percentage.search(message) and pattern_numbers.search(message):
        return True
    if pattern_ad.search(message):
        return True
    if pattern_month.search(message) and (pattern_vip.search(message) or pattern_stock.search(message)):
        return True
    
    # If none of the patterns match, the message is not spam
    return False