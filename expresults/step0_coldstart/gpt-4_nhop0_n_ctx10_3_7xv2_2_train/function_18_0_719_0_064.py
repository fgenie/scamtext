def is_spam(message):
    
    import re

    # Find specific keywords that are commonly seen in spam messages.
    spam_keywords = ["추천주", "정보 및", "수익률", "상한가", "%.업", "주식.*공시", "익 절", "상세히", "클릭", "전문가", "적중", "누적수익률"]

    # Check if a keyword is present in the message.
    for keyword in spam_keywords:
        if re.search(keyword, message):
            return True

    # Check for shortened URLs, which are commonly used in spam messages.
    url_pattern = re.compile(r'(http(s)?://\S+bit\.ly|http(s)?://\S+me2\.kr|http(s)?://\S+ko\.gl|fastkakao\.com|opcn-kakao\.com)')
    urls = url_pattern.findall(message)
  
    if len(urls) > 0:
        return True

    message_length = len(message)

    # Errors or special characters in the message that are commonly found in spam messages.
    errors_sp_char = ["\n", "^", "~", "*", "!", "＼", "_", ",", ":", "…", "·", "‧", "□", "【", "｜", "｛"]

    errors_counter = 0
    for special_char in errors_sp_char:
        errors_counter += message.count(special_char)
        
    # Calculate the ratio of errors or special characters to the message length.
    errors_ratio = errors_counter / message_length
    
    if errors_ratio > 0.1:
        return True

    return False