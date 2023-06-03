
import re

def is_spam(message: str) -> bool:
    """
    Checks if the given message is spam.

    :param message: str
        The message to be classified as spam or not.
    :return: bool
        True if the message is spam, False otherwise.
    """
    # Check for the presence of url shorteners
    url_shorteners = ['bit.ly', 'me2.kr', 'af44']
    for shortener in url_shorteners:
        if shortener in message:
            return True

    # Check for non-Unicode characters and existence of multiple symbols
    non_alphanumeric = re.findall(r'\W', message)
    symbols_count = len(non_alphanumeric)
    total_message_length = len(message)
    
    if symbols_count / total_message_length > 0.3 or len(set(non_alphanumeric)) > 5:
        return True

    return False
