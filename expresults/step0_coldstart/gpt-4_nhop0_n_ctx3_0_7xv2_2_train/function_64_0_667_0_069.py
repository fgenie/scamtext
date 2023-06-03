def is_spam(message):
    import re

    # Check for common spam keywords
    spam_keywords = ["특파원", "추천주", "상한가", "공개합니다", "클릭후", "유료 전환", "실력입증", "차별화된 정보", "이벤트 참여", "무료입장", "수익률", "단독발표정보", "참여하세요", "체험반", "평균 수익률", "목표가", "화성 30%↑", "공시발표 전", "상한가 확정", "파이널 VIP", "만나보세요"]

    for keyword in spam_keywords:
        if keyword in message:
            return True

    # Check if message contains suspicious URLs
    url_pattern = re.compile(r'(https?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\\(\\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+)')
    urls = url_pattern.findall(message)
    
    for url in urls:
        # Check for URL shorteners, which are common in spam messages
        shorteners = ["me2.kr", "vo.la", "bit.ly", "goo.gl", "ow.ly", "tinyurl.com"]

        for shortener in shorteners:
            if shortener in url:
                return True
                
    # Check for excessive number of special characters
    special_chars_pattern = re.compile(r'[!%/|^~&`\[\]]+')
    special_chars = special_chars_pattern.findall(message)
    
    if len(special_chars) > 4:  # Threshold for excessive number of special characters
        return True

    # If none of the spam conditions are met, return False, meaning it's not a spam
    return False