def is_spam(message: str) -> bool:
    import re
    import string

    # Check for URL shorteners, common in spam messages
    short_url_regex = r"(https?:\/\/)?([\da-z\.-]+)\.([a-zA-Z\.]{2,6})([\/\w\.-]*)"
    short_urls = re.findall(short_url_regex, message)
    if len(short_urls)>0:
        return True
        
    # Check for excessive punctuation, common in spam messages
    punctuation_count = sum([1 for char in message if char in string.punctuation])
    if punctuation_count / len(message) > 0.2:
        return True

    # Check for words common in spam messages
    spam_keywords = ['추천주', '현황', '수익률', '체험', '이벤트', '공개', '상승', '무료', 'VIP']
    count_keywords = sum([1 for keyword in spam_keywords if keyword in message])
    if count_keywords > 1:
        return True

    return False