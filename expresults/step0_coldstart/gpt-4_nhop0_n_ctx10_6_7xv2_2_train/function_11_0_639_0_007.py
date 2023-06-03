def is_spam(message):
    import re
    
    # Check for (광고) at the beginning of the message
    if message.startswith("(광고)"):
        return True
    
    # Check for certain keywords typically found in spam messages
    spam_keywords = ["성과", "이벤트", "지원받고", "지원금", "적중", "발표시", "급등예정", "매수매도타점공유", "수익금", "연봉창출", "체계적 교육 제공", "지인추천 이벤트", "무료거부"]
    for keyword in spam_keywords:
        if keyword in message:
            return True
    
    # Check for suspicious URLs using regex
    suspicious_url_patterns = [
        r"https?:\/\/bit\.ly\/\w+",
        r"https?:\/\/me2\.kr\/\w+",
        r"https?:\/\/han\.gl\/\w+",
        r"https?:\/\/vo\.la\/\w+"
    ]
    for pattern in suspicious_url_patterns:
        if re.findall(pattern, message):
            return True

    # Check for excessive capitalization
    capitalized_words = re.findall(r"\b[A-Z]{3,}\b", message)
    if len(capitalized_words) > 3:
        return True

    return False