def is_spam(message: str) -> bool:
    import re

    # Check if message contains a URL
    url_pattern = re.compile(r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\\(\\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+')
    contains_url = re.search(url_pattern, message)

    # Check if message contains any numbers followed by special characters
    spam_pattern = re.compile(r'\d+[\]\(ㄷ)>월시\-=+!@(ги )]+')
    is_spammy = re.search(spam_pattern, message)

    # Check for any stock code
    stock_code_pattern = re.compile(r'\([0-9]{5,6}\)')
    contains_stock_code = re.search(stock_code_pattern, message)

    # Define basic conditions
    if contains_url and (is_spammy or contains_stock_code):
        return True
    elif is_spammy:
        return True
    else:
        return False