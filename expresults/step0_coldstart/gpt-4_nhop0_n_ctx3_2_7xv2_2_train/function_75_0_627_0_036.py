def is_spam(message):
    import re

    # Check for specific spam indicators
    url_regex = r'(?:http|ftp|https)://(?:[\w_-]+(?:(?:\.[\w_-]+)+))(?:[\w.,@?^=%&:/~+#-]*[\w@?^=%&/~+#-])?'
    spam_indicators = ['정회원방', '처음\d', 'BBQ', '피자', '활쿱', '전화X', '코드:자동']

    # If the message contains a URL
    if re.search(url_regex, message):
        return True

    # If the message contains any of the spam indicators
    for indicator in spam_indicators:
        if indicator in message:
            return True

    # If none of the spam indicators are found, it's not spam
    return False