def is_spam(message):
    import re

    # Check for spam keywords
    spam_keywords = ['광고', 'VIP', 'EVENT', '진행', 'code', '적립금', '게임', '무료거부', '바［CA］ㄹ', '종목', '대형', 'Major']

    for keyword in spam_keywords:
        if keyword in message:
            return True

    # Check for URLs
    url_pattern = re.compile(r'https?://\S+|www\.\S+')
    if url_pattern.search(message):
        return True
    
    # Check for special characters
    special_char_pattern = re.compile(r'[!@#$%^&*()_=+[\]{}\\\\|;:",.<>?/\-`~─｜]')
    special_char_count = len(special_char_pattern.findall(message))
    if special_char_count > 2:
        return True
    
    # Check for excessive use of numbers
    numbers_pattern = re.compile(r'\d+')
    nums = numbers_pattern.findall(message)
    numbers_count = sum(len(num) for num in nums)
    if numbers_count > 6:
        return True

    return False