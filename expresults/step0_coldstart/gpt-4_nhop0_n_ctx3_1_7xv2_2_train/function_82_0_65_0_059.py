def is_spam(message: str) -> bool:
    import re
    
    keywords = ['긴급입수정보', '상한가', '무료체험반', '해 외 선 물', '경제적 자유', '베팅', '초급~심화과정',
                '배움의길', '방송하는 이선생', '세력 매집주', '비공개 상승주']
    
    # Check for presence of keywords
    for keyword in keywords:
        if keyword in message:
            return True
    
    # Check for presence of URL
    url_pattern = r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\\(\\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+'
    if re.findall(url_pattern, message):
        return True

    # Check for excessive use of special characters
    special_chars = '!,@,_,$,&'
    special_chars_count = sum([message.count(c) for c in special_chars])
    if special_chars_count / len(message) > 0.2:
        return True
    
    return False