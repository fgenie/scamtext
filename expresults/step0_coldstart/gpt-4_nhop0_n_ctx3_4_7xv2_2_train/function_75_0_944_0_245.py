def is_spam(message):
    import re

    # Check for spam keywords and suspicious percentage signs
    keywords = ['VIP', '비공개', '추천', '돌파', '타점']
    keywords_found = any(keyword in message for keyword in keywords)

    percentage_sign_found = '%' in message

    # Check for URLs
    url_pattern = re.compile(r'(https?://\S+)')
    url_found = bool(re.search(url_pattern, message))

    # Check for message length
    long_message = len(message.split()) > 6

    if keywords_found or percentage_sign_found or url_found or long_message:
        return True
    else:
        return False