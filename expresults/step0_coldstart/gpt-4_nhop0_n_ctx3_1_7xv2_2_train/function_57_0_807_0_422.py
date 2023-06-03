def is_spam(message):
    import re
    
    # Check for excessive capitalization and special characters
    capital_ratio = sum(1 for c in message if c.isupper()) / len(message)
    special_chars_ratio = len(re.findall(r'\W', message)) / len(message)
    
    if capital_ratio > 0.4 or special_chars_ratio > 0.25:
        return True

    # Check for common spam words/phrases
    spam_keywords = ['대박', '수익', '투자계획', '하락장', '진입 장벽', '연이은', '유튜브', '두눈으로', '최근 3개월', '매매 성과']
    for keyword in spam_keywords:
        if keyword in message:
            return True

    # Check for suspicious URLs
    urls = re.findall(r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\\(\\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', message)
    if len(urls) > 1:
        return True
    
    # If none of the above conditions are met
    return False