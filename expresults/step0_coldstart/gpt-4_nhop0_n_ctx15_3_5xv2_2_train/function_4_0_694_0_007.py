def is_spam(message: str) -> bool:
    import re
    
    # Check for common spam phrases/words
    spam_phrases = ['spam', '광고', '회원', '알림', '입장','지원','선입금','공짜','특가','회원세일','할인','장터']
    for phrase in spam_phrases:
        if phrase in message:
            return True
    
    # Check for excessive special characters
    special_char_count = len(re.findall(r'[!@#$%^&*(),.?":{}|<>]', message))
    if special_char_count / len(message) > 0.5:
        return True
    
    # Check for excessive capital letters
    capital_char_count = len(re.findall(r'[A-Z]', message))
    if capital_char_count / len(message) > 0.5:
        return True
    
    # Check for excessive usage of digits
    digit_count = len(re.findall(r'\d', message))
    if digit_count / len(message) > 0.4:
        return True
    
    # Check for suspicious URLs
    suspicious_urls = ['bit.ly', 'me2.kr', '.profit', 'money.', 'income.', 'earn', 'cash', 'investment']
    for url in suspicious_urls:
        if url in message:
            return True
            
    return False