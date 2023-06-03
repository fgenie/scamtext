
import re

def is_spam(message: str) -> bool:
    """
    Determine if a given message is a spam or not.

    :param message: message content as a string
    :return: True if the message is a spam, False otherwise
    """

    # Check for special characters and numbers frequently used in spam messages
    special_char_pattern = r"[!@#$%^&*()_+={}\[\]|\\,.:;?<>]"
    numbers_pattern = r"\d"
    special_char_count = len(re.findall(special_char_pattern, message))
    numbers_count = len(re.findall(numbers_pattern, message))
    
    message_words = message.split()
    message_length = len(message_words)

    # Check for presence of a URL and short URL services
    url_pattern = r"(https?://\S+|www\.\S+|bit\.ly/\S+|me2\.kr/\S+)"
    url_count = len(re.findall(url_pattern, message))

    # Calculate the ratio of special character, numbers and URLs to the total length of the message
    special_char_ratio = special_char_count / (message_length + 1)
    numbers_ratio = numbers_count / (message_length + 1)
    url_ratio = url_count / (message_length + 1)

    # If the message has a high special character, numbers, or URL ratio, it is likely spam
    if special_char_ratio > 0.15 or numbers_ratio > 0.4 or url_ratio > 0.2:
        return True

    return False
