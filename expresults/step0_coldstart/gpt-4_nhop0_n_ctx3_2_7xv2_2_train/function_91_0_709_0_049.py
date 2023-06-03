def is_spam(message):
    import re
    
    # Rule 1: Check for unusual URLs
    unusual_url_pattern = r'https?://\w+\.\w{1,2}/\w{1,2}/?'
    found_unusual_url = bool(re.search(unusual_url_pattern, message))
    
    # Rule 2: Check for too many percentage symbols in the message
    percentage_symbols = message.count('%')
    too_many_percentages = percentage_symbols > 1
    
    # Rule 3: Check for generic stock-related keywords
    stock_keywords = ['적중', '종목', '수익률']
    found_stock_keywords = any(keyword in message for keyword in stock_keywords)

    # Classify as spam if any one of the rules is triggered
    if found_unusual_url or too_many_percentages or found_stock_keywords:
        return True
    else:
        return False