def is_spam(text):
    import re
    
    # Check for presence of amount and currency symbols
    amounts = re.findall(r"(\d{1,3}(?:,\d{3})*\.\d{2}|\d{1,3}(?:,\d{3})*\d{2})", text)
    currency_symbols = re.findall('[₩$€¥£]', text)
    
    # Check for multiple links
    links = re.findall('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\\(\\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', text)
    
    # Check for excessive use of special characters
    special_chars = re.findall('[^a-zA-Z0-9가-힣]', text)
    
    if amounts or currency_symbols or (len(links) > 1) or (len(special_chars) > len(text) / 2):
        return True
    else:
        return False