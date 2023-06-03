def is_spam(message):
    import re

    # Check for presence of URLs
    url_pattern = re.compile(r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+')
    url_count = len(re.findall(url_pattern, message))
    
    # Check for presence of keywords related to spam
    spam_keywords = ['상한가', '추천주', '독점공급', 'AI사업', 'MOU', '종목명']
    keyword_count = sum([message.count(keyword) for keyword in spam_keywords])
    
    # Check for excessive characters and special characters not commonly used in normal messages
    excess_chars = re.findall(r'[^가-힣\s\w\.]+', message)
    
    # If any of the spam criteria is met, classify the message as spam
    if url_count > 0 or keyword_count > 0 or excess_chars:
        return True
    else:
        return False