def is_spam(message):
    import re

    spam_keywords = [
        "돌파", "종목", "카카오톡", "매수", "계좌", "추천", "경제", "수익",
        "공개", "성공", "상승", "달성", "80003705780", "시장", "주의",
        "주식", "투자", "통합운영", "하이빌", "거래", "달러", "확인", "신규",
        "천억", "금융", "소장", "늘어나", "포트폴리오"
    ]

    url_pattern = re.compile(r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\\(\\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+')
    
    # Count the number of keywords in the message
    keyword_count = 0
    for keyword in spam_keywords:
        keyword_count += message.count(keyword)
        
    # Check if the message contains a URL
    url_found = bool(url_pattern.search(message))
    
    # If the message contains at least 2 keywords and a URL, it is considered spam
    return keyword_count >= 2 and url_found