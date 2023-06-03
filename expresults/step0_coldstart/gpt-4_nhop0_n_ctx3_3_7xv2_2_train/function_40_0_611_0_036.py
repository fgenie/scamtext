def is_spam(message):
    import re

    # List of spam keywords
    spam_keywords = ['투자', 'VIP', ' 체험', '매수', '연혁', '시황', '월수익', '추천종목', '무료거부']
    url_pattern = re.compile(
        r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+')

    # Count the number of spam keywords in the message
    spam_keywords_count = sum([1 for keyword in spam_keywords if keyword in message])
    
    # Check if the message contains URLs
    urls = re.findall(url_pattern, message)

    # If more than half of the spam keywords are present or if there is an URL in-message, it's likely spam
    if spam_keywords_count >= len(spam_keywords) / 2 or len(urls) > 0:
        return True

    return False