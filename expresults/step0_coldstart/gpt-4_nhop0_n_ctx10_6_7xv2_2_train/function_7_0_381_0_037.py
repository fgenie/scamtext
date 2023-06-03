def is_spam(text: str) -> bool:
    import re

    spam_keywords = [
        "수익",
        "상한가",
        "최대",
        "할인",
        "100%",
        "단독제휴",
        "유튜브",
        "카카오톡",
        "지급",
        "주가",
        "투자",
        "증권",
        "최고급",
        "공시",
        "작전",
        "고급정보",
        "무료수신거부",
        "수익률",
        "장점",
        "kb증권",
    ]
    
    normal_keywords = [
        "안녕",
        "여기와라",
        "넵",
        "거 봤음?",
        "진행해서",
        "업데이트",
    ]
    
    # Remove special characters and URLs
    text = re.sub(r"[^가-힣0-9A-Za-z\s]+", "", text)
    text = re.sub(r"https?:\/\/[^\s]+", "", text).lower().strip()

    spam_count = sum([1 for word in spam_keywords if word.lower() in text])
    normal_count = sum([1 for word in normal_keywords if word.lower() in text])

    return spam_count > normal_count