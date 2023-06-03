def is_spam(message):
    import re

    # Check for presence of urls
    url_pattern = re.compile(r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\\(\\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+')
    url_exists = bool(url_pattern.search(message))

    # Check for presence of numbers mixed with special characters or units of currency
    mix_pattern = re.compile(r'[\d,.]+[원달러만천백]{0,}[.!?,;%]+|[% -][\d,.]+[원달러만천백]{0,}')
    mix_exists = bool(mix_pattern.search(message))

    # Check for the presence of common scam-related keywords
    keywords = ['출금', '수익', '투자', '혜택', '증권', '대출', '금융', '체험', '무료']
    keyword_exists = any(keyword in message for keyword in keywords)

    return url_exists or mix_exists or keyword_exists