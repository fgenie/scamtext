def is_spam(message: str) -> bool:
    import re
    
    # Thresholds
    min_ad_keywords = 2
    min_emojis = 3
    ad_keywords = [
        "광고", "선물", "이벤트", "대회", "한정", "특별", "혜택",
        "증권", "부동산", "코인", "자금", "거래", "특가",
        "(주)", "매수", "hts", "mts", "하기",
        "무료", "참여", "신규", "지원", "가입", "쿠폰", "할인",
        "기회", "치킨", "주십니까"
    ]
    ad_pattern = "|".join(ad_keywords)
    
    # Emoji pattern
    emoji_pattern = re.compile(
        "["
        u"\U0001F600-\U0001F64F"  # emoticons
        u"\U0001F300-\U0001F5FF"  # symbols & pictographs
        u"\U0001F680-\U0001F6FF"  # transport & map symbols
        u"\U0001F1E0-\U0001F1FF"  # flags (iOS)
        u"\U00002702-\U000027B0"
        u"\U000024C2-\U0001F251"
        "]+", flags=re.UNICODE
    )

    # Check for common ad keywords
    ad_count = sum(1 for _ in re.finditer(ad_pattern, message.lower()))
    
    # Check if the message has too many emojis
    emoji_count = len(emoji_pattern.findall(message))
    
    # Classify the message as spam if the conditions are met
    return ad_count >= min_ad_keywords or emoji_count >= min_emojis