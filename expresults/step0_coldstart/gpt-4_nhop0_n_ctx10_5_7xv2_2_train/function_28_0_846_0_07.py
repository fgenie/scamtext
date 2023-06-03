import re

def is_spam(message):
    # Define patterns related to spam messages
    url_pattern = r'https?://[\w\-\.]+'
    consecutive_caps_pattern = r'[A-Z]{2,}'
    repetitive_chars_pattern = r'([a-zA-Z])\1{3,}'
    spam_keywords = ['광고', '매매', '증권', '수익', '무료', '이벤트', '상한가', '발표']

    # Check if the message contains a URL
    if re.search(url_pattern, message):
        return True

    # Check if the message contains consecutive capital letters
    if re.search(consecutive_caps_pattern, message):
        return True

    # Check if the message contains repetitive characters
    if re.search(repetitive_chars_pattern, message):
        return True

    # Check if the message contains spam keywords
    for keyword in spam_keywords:
        if keyword in message:
            return True

    return False