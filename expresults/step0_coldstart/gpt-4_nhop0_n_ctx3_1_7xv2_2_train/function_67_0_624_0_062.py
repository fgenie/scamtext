def is_spam(message):
    import re

    # Rule 1: Check for url shortening services
    shortened_urls = re.findall(r'(bit\.ly|me2\.kr)\/\S+', message)
    if shortened_urls:
        return True

    # Rule 2: Check for special characters used repetitively
    special_char_pattern = r'[!~*]{2,}'
    if re.search(special_char_pattern, message):
        return True

    # Rule 3: Check for stock or investment related keywords
    stock_keywords = ["종목추천", "연상", "미리입장", "투자", "이동", "정식허가", "국내식약처"]
    for keyword in stock_keywords:
        if keyword in message:
            return True

    return False