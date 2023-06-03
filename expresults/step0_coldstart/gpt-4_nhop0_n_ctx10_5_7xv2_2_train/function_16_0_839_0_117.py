def is_spam(message):
    import re

    # Keywords for spam detection
    spam_keywords = ['↑', '광고', '만원', '수익', '정회원', '선물지수', '계신', '참여', '연속', '가루', '할인', '매직', '강추',\
                    '링크', '방문', '톡방', '할인코드', '프로모션', 'izz', '독점', '상한가']

    # Check for spam keywords
    for keyword in spam_keywords:
        if keyword.lower() in message.lower():
            return True

    # Check for urls that are not typical
    url_pattern = re.compile(r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+')
    url_matches = re.findall(url_pattern, message)
    for url in url_matches:
        if not any(common_site in url for common_site in ['google.com', 'youtube.com', 'amazon.com', 'facebook.com', 'wikipedia.org']):
            return True

    # Check for excessive use of special characters
    special_chars = ['!', '@', '#', '$', '%', '&', '*', '(', ')', '_', '+']
    special_char_count = sum([1 for c in message if c in special_chars])
    if special_char_count / len(message) > 0.05:
        return True

    # Check for phone numbers
    phone_number_pattern = re.compile(r'(\d{2,4})\D{0,3}(\d{3,4})\D{1}(\d{4})')
    if phone_number_pattern.search(message):
        return True

    return False