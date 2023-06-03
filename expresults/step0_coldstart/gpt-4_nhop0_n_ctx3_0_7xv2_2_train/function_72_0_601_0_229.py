def is_spam(text):
    import re

    # Check for special characters and excessive use of symbols
    if re.search(r'[-=+,#/\?:^$.@*\"※~&%ㆍ!』\\‘’|\(\)\[\]\<\>`\'…》]', text):
        special_chars = len(re.findall(r'[-=+,#/\?:^$.@*\"※~&%ㆍ!』\\‘’|\(\)\[\]\<\>`\'…》]', text))
        if special_chars > len(text) * 0.1:  # Adjust the threshold as needed
            return True

    # Check for excessive use of capital letters or numbers
    uppercase_letters = len(re.findall(r'[A-Z]', text))
    digits = len(re.findall(r'\d', text))
    if uppercase_letters > len(text) * 0.3 or digits > len(text) * 0.3:  # Adjust the threshold as needed
        return True

    # Check for known spam-specific phrases or patterns
    spam_phrases = ['무료수신거부', '특별찬스', '안전한토토사이트추천', '토토사이트주소']
    for phrase in spam_phrases:
        if phrase in text:
            return True

    # Check for URLs with suspicious patterns
    suspicious_urls = re.findall(r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\\(\\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', text)
    for url in suspicious_urls:
        if "opcn-kakao.com" in url or "-zxc.com" in url:
            return True
            
    return False