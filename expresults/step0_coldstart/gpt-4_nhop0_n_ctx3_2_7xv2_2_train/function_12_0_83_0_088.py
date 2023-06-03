def is_spam(message: str) -> bool:
    import re
    
    # Check for common spam keywords
    spam_keywords = [
        "당첨", "무료", "보증", "수익", "투자", "진행중", "광고", "비용", "계약", "가입", "금전요구", "이벤트", "상품", "적립", "할인", "한정"
    ]
    
    for keyword in spam_keywords:
        if keyword in message:
            return True
    
    # Check for URL patterns
    url_pattern = re.compile(r'(http|https|www\.)\S+|me2\.kr/\S+|bit\.ly/\S+|openkakao\..*?/dsa')
    urls = re.findall(url_pattern, message)
    if len(urls) > 0:
        return True

    # Check for numbers followed by uncommon symbols
    number_pattern = re.compile(r'\d+[,.]+(?:[^A-Za-z\d\s]+?)')
    numbers = re.findall(number_pattern, message)
    if len(numbers) > 0:
        return True
    
    return False