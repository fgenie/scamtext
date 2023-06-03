def is_spam(message: str) -> bool:
    import re

    # Check for multiple occurrences of the same message
    if message.count(message[:10]) > 1:
        return True

    # Check for urls
    url_pattern = re.compile(r'(http[s]?://|me2|han.gl)[^ ]+')
    urls = url_pattern.findall(message)
    if len(urls) > 0 and any(['bit.ly' in url or 'me2.kr' in url or 'han.gl' in url for url in urls]):
        return True

    # Check for percentages and other spam indicators
    percent_pattern = re.compile(r'\d+%')
    if percent_pattern.search(message) and ('상승' in message or '증가' in message):
        return True

    # Check for word patterns commonly found in spam messages
    spam_words = ["추천주", "체험반", "무료", "상한가", "VIP"]
    if any([word in message for word in spam_words]):
        return True

    return False