def is_spam(message):
    import re

    # Check for common spam keywords and excessive use of special characters
    spam_keywords = ['추천주', '원 금', '만들기', '투자', '성공', '프로젝트', '주식', '혜택', '배워보기', '만원']
    special_chars = ['$', '%', '↑', '▼']

    spam_index = 0
    for keyword in spam_keywords:
        if keyword in message:
            spam_index += 1

    special_char_count = sum([1 for char in message if char in special_chars])

    if special_char_count > 2:
        spam_index += 1

    # Look for suspicious URLs
    url_pattern = re.compile(r'https?://[\w\-.]+(?:\.[\w\-.]+)+\S*\b')
    url_indices = [match.start() for match in re.finditer(url_pattern, message)]

    if len(url_indices) != 0:
        for index in url_indices:
            if message[max(0, index-5):index].strip(' ') not in ('→', '↗', '↘', '↗line', '|'):
                spam_index += 1
    
    return spam_index >= 3