
import re

def is_spam(message):
    """
    Check if the given message can be classified as spam.

    Args:
    message (str): The message to be classified

    Returns:
    bool: True if message is spam, False otherwise
    """

    # Check for common spam features such as excessive use of special characters
    special_chars = re.findall(r'[^\w\s]', message)
    if len(special_chars) / len(message) > 0.2:
        return True

    # Check for commonly used spam phrases
    spam_phrases = [
        '명-가', '핫', 'B.H당', '적립',
        '안전', '확률', '종목', '수익', '대형'
    ]
    if any(phrase in message for phrase in spam_phrases):
        return True

    # Check for suspicious URLs
    spam_urls = re.findall(r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\\(\\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', message)
    if len(spam_urls) > 0:
        return True

    # If none of the above conditions are met, the message is considered normal
    return False
