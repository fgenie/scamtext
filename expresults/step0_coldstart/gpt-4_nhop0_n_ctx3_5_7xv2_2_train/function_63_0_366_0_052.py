def is_spam(message):
    import re
    
    spam_keywords = ["상한가", "공시발표", "투자반", "단기수익", "무료거부", "신규인원", "약속", "보상", "공개", "주식", "MOU체결", "분석/추천/시황", "완판", "성공률",
                     "안 사셔도 됩니다!", "강요하지 않습니다!", "지켜 만 보셔도 됩니다!"]

    message = message.lower()
    for keyword in spam_keywords:
        keyword = keyword.lower()
        if keyword in message:
            return True
            
    url_pattern = re.compile(r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+')
    url_count = len(re.findall(url_pattern, message))
    if url_count >= 2:
        return True

    return False