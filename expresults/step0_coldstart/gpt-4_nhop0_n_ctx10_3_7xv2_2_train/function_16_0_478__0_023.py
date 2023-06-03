def is_spam(message: str) -> bool:
    import re
    
    # Check for common spam phrases
    spam_phrases = [
        "목표달성기념",
        "수익 종목",
        "추천주 현황",
        "급등예정 종목",
        "VIP체험반",
        "프로모션",
        "바로입장",
        "매매 성과",
        "선물지급",
        "강의 및 교육"
    ]
    
    for phrase in spam_phrases:
        if phrase in message:
            return True
    
    # Check for suspicious URLs
    urls = re.findall(r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\\(\\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', message)
    spam_domains = [
        "me2.kr",
        "openkakao",
        "gg.gg",
        "선물지급.com"
    ]
    
    for url in urls:
        for domain in spam_domains:
            if domain in url:
                return True

    return False