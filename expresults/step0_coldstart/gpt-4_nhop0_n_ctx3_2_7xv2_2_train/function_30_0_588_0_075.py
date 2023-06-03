def is_spam(message: str) -> bool:
    import re

    # Set thresholds for classification
    url_threshold = 1
    number_threshold = 3

    # Identify number of URLs in the message
    url_pattern = r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\\(\\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+'
    urls = re.findall(url_pattern, message)
    url_count = len(urls)

    # Identify number of numerical sequences in the message
    number_pattern = r'\d+'
    numbers = re.findall(number_pattern, message)
    number_count = len(numbers)

    # Check if the message contains specific spam keywords
    spam_keywords = ["무료거부", "체험반", "수익률", "연상", "정력"]

    contains_spam = False
    for keyword in spam_keywords:
        if keyword in message:
            contains_spam = True
            break

    # Classify the message as spam if it meets any of the following conditions:
    # - Contains more URLs than the threshold
    # - Contains more numerical sequences than the threshold
    # - Contains spam keywords
    if url_count > url_threshold or number_count > number_threshold or contains_spam:
        return True

    return False