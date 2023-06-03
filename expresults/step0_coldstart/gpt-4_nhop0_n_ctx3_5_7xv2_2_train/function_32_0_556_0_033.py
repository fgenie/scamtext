def is_spam(message):
    import re

    # Check for URL containing suspicious domain names.
    url_pattern = re.compile(r'(https?://[-A-Za-z0-9@:%._\+~#=]{1,256}\.[A-Za-z]{2,6}\b([-A-Za-z0-9@:%_\+.~#?&//=]*))')
    urls = url_pattern.findall(message)
    suspicious_domains = ['opcn-kakao.com', 'kakaotalk.at', 'me2.kr']
    
    for url, _ in urls:
        for domain in suspicious_domains:
            if domain in url:
                return True

    # Check for keywords that might indicate a spam message.
    spam_keywords = ['신청하신', '입장 안내', 'VIP방', '고수익', '축하드립니다', '다음타자']
    for keyword in spam_keywords:
        if keyword in message:
            return True

    # Check for unusual repetition in message.
    consec_chars_pattern = re.compile(r'(.)\1{3,}')
    if re.findall(consec_chars_pattern, message):
        return True

    return False