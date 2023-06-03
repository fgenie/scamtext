import re

def is_spam(text: str) -> bool:
    # Check for spam keywords and patterns
    spam_keywords = ['광고', '거부', '클릭', '해지', '이벤트', '공짜', '하세요', '무료', '최고', '상위', '증권사', '특별', '혜택', '무료거부', '입장코드', '특별정보방', '여의도', '입장', '금전'] 

    # Check for URL patterns
    url_pattern = re.compile(r'(http|https)://\S+')

    # Check for phone number patterns
    phone_pattern = re.compile(r'\d{2,4}-\d{3,4}-\d{4}')

    # Check for non-normal characters
    non_normal_chars = re.compile(r'[^가-힣a-zA-Z0-9.,?!:;\-\s]+')

    # Count the number of spam indicators
    spam_count = 0

    # Check for spam keywords
    for keyword in spam_keywords:
        if keyword in text:
            spam_count += 1

    # Check for URL patterns
    if url_pattern.search(text) is not None:
        spam_count += 1

    # Check for phone number patterns
    if phone_pattern.search(text) is not None:
        spam_count += 1

    # Check for non-normal characters
    if non_normal_chars.search(text) is not None:
        spam_count += 1

    # If more than 1 spam indicators are detected, classify the message as spam
    if spam_count >= 2:
        return True
    
    return False