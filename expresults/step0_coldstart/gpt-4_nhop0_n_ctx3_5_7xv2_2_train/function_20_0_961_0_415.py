def is_spam(message):
    import re

    # Check for presence of URL
    url_pattern = re.compile(r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\\(\\),]"|(?:%[0-9a-fA-F][0-9a-fA-F]))+')
    urls = url_pattern.findall(message)

    # Check for non-Korean characters and special words
    non_korean_pattern = re.compile(r'[^\uac00-\ud7a3\s]')
    special_words = ['적중', '체험', '정보방', '선택의 기회']
    spam_indicator_count = 0

    for word in special_words:
        if word in message:
            spam_indicator_count += 1
      
    spam_indicator_count += len(urls)
    spam_indicator_count += len(non_korean_pattern.findall(message))

    # Consider a message as spam if there are more than two indicators
    if spam_indicator_count >= 2: 
        return True

    return False