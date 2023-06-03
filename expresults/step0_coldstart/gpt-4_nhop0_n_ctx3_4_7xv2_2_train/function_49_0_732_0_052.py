def is_spam(message: str) -> bool:
    import re
    
    # Check for presence of URLs
    url_pattern = re.compile(r'(http|https|ftp)://[a-zA-Z0-9\-\.]+\.[a-zA-Z]{2,3}(/\S*)?')
    if url_pattern.search(message):
        return True

    # Check for presence of percentage sign (%)
    if "%" in message:
        return True

    # Check for presence of unicode characters
    if re.search(r'[\u4e00-\u9FFF]+', message):
        return True

    # Check for presence of stock codes
    stock_code_pattern = re.compile(r'\([0-9]{6}\)')
    if stock_code_pattern.search(message):
        return True
    
    return False