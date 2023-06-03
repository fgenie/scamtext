def is_spam(message):
    import re

    # Check for spam keywords
    spam_keywords = ['원', '최소', '클릭', '종목확인', '익 절 가', '수익률']
    for keyword in spam_keywords:
        if keyword in message:
            return True

    # Check for urls
    url_pattern = re.compile(r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\\(\\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+')
    urls = re.findall(url_pattern, message)
    if urls:
        return True

    # Check for percentages
    percentage_pattern = re.compile(r'\+*\d+(\.\d{1,2})*%')
    percentages = re.findall(percentage_pattern, message)
    if percentages:
        return True

    # Check for sequences of numbers
    numbers_pattern = re.compile(r'\d+')
    numbers = re.findall(numbers_pattern, message)
    if len(numbers) > 3:
        return True

    return False