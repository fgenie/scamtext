def is_spam(message: str) -> bool:
    import re

    # Check for urls and money related keywords
    url_pattern = r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\\(\\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+'
    money_pattern = r'\b(?:원|돈|투자|마감|다음[\s]*타자|배워보기|부자|미래|만들기)\b'

    # Count number of urls and money related keywords
    url_count = len(re.findall(url_pattern, message))
    money_count = len(re.findall(money_pattern, message))

    # Check for excessive use of symbols and special characters
    symbols = r'[\*\.\-\_/\\\:=▼]'
    symbols_count = len(re.findall(symbols, message))

    # Check if the message is too short
    is_short = False
    if len(message.strip()) < 10:
        is_short = True

    if url_count > 0 or symbols_count >= 5 or (money_count >= 2 and is_short):    
        return True
    return False