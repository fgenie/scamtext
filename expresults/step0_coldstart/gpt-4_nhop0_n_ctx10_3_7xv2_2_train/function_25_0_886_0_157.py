def is_spam(message):
    import re

    # Check for keywords typically found in spam messages
    spam_keywords = ['광고', 'VIP', '투자', '상담', '수익', '추천종목', '특별케어', '실리콘', '주식']

    for keyword in spam_keywords:
        if keyword in message:
            return True

    # Check for URLs in the message
    url_pattern = re.compile(r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\\(\\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+')
    urls = re.findall(url_pattern, message)
    if len(urls) > 0:
        return True

    # Check for excessive use of numbers or special characters
    num_pattern = re.compile(r'\d')
    special_char_pattern = re.compile(r'[\W_]+')

    num_count = len(re.findall(num_pattern, message))
    special_char_count = len(re.findall(special_char_pattern, message))

    if num_count > 5 or special_char_count > 10:
        return True

    # If none of the above conditions are met, consider the message as normal
    return False