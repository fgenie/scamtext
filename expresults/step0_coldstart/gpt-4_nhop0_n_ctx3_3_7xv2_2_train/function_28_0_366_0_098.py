def is_spam(message):
    import re
    
    # Check for spam keywords
    spam_keywords = ['수혜주', '투자', '주식', 'MOU추진', '발표확정', '자산가', '수익달성', '클릭하시면', '클릭', '알려드린', '으면', '수익방법']
    if any(keyword in message for keyword in spam_keywords) or len(re.findall(r'https?://\S+', message)) > 1:
        return True
    
    # Check for long sequences of symbols or special characters
    symbol_regex = r'[%\-_=/\\]+|[\*]+'
    matches = re.findall(symbol_regex, message)
    if any(len(symbols) > 3 for symbols in matches):
        return True

    # Check for phoneNumber
    phone_regex = r'\d{2,4}-\d{3,4}-\d{3,4}'
    if re.search(phone_regex, message) is not None:
        return True

    # Check for consecutive capital letters
    caps_regex = r'\b[A-Z]{2,}\b'
    if re.search(caps_regex, message) is not None:
        return True
        
    # Check for excessive use of exclamation points or question marks
    if message.count('!') > 3 or message.count('?') > 3:
        return True
      
    return False