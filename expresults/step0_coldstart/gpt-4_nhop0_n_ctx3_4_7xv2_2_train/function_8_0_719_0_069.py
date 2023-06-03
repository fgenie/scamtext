def is_spam(message):
    import re
    
    # Lowercase the message
    message = message.lower()
    
    # Check for suspicious keywords
    spam_keywords = ["만원", "광고]", "kakaotalk.at", "목표가", "방영", "상승", "정보", "비용", "거래량", "최.소", "사활"]
    for keyword in spam_keywords:
        if keyword in message:
            return True
    
    # Check for suspicious URL patterns
    url_pattern = r"http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+"
    urls = re.findall(url_pattern, message)
    if len(urls) > 0:
        return True
    
    # Check for suspicious repetition patterns
    repetition_pattern = r"(\w{2,})\1{2,}"
    repetitions = re.findall(repetition_pattern, message)
    if len(repetitions) > 0:
        return True

    return False