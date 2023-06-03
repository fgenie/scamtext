def is_spam(text):
    import re
    
    spam_keywords = [
        "비밀번호", "회사공시", "목표가", "익절가", "수익률", "VIP체험", "모집합니다",
        "종목확인", "무료교육", "할인", "(광고)", "거래방법", "클릭+", "방문하세요",
        "무료거부", "소식받았어요", "파워콘텐츠"
    ]
    
    normal_keywords = [
        "네이버", "KB국민", "카드 영업점", "문의", "고객센터", "엄마", "아빠"
    ]
    
    # Remove special symbols and urls from text
    clean_text = re.sub(r"http[a-zA-Z0-9\-\:\.\/\_]+|\W+", " ", text)
    
    # Check if keyword matches any known spam keywords
    for spam_keyword in spam_keywords:
        if spam_keyword in clean_text:
            return True
    
    # Check if keyword matches any known normal keywords
    for normal_keyword in normal_keywords:
        if normal_keyword in clean_text:
            return False
    
    # If no spam keywords and normal keywords matched, consider it as normal if 
    # text size is less than 150 characters
    if len(clean_text) < 150:
        return False
    
    return True