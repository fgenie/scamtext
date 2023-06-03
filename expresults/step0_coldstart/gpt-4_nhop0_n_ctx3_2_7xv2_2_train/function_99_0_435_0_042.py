
import re

def is_spam(text):
    """
    This function checks if a given text is a spam message or not.

    Args:
    text (str): the input message as a string

    Returns:
    bool: True if the message is spam, otherwise, False
    """
    # Feature 1: Check if the text contains a URL
    url_pattern = r'https?://(?:[-\w.]|(?:%[\da-fA-F]{2}))+'
    contains_url = bool(re.search(url_pattern, text))

    # Feature 2: Check if the text contains a high percentage of special characters
    special_chars_pattern = r'[\W_]'
    special_chars_percentage = len(re.findall(special_chars_pattern, text)) / len(text)
    high_special_chars = special_chars_percentage >= 0.3

    # Feature 3: Check if the text contains percentage signs and numerals
    contains_percentages = bool(re.search(r'\d+%+', text))
    
    # Feature 4: Check if the text contains multiple consecutive upper case words
    upper_case_count = sum([bool(re.match(r'^[A-Z]+$', word)) for word in text.split()])
    consecutive_upper_case = upper_case_count >= 2

    # If at least two of the above features are True, consider the message as spam
    spam_features = [contains_url, high_special_chars, contains_percentages, consecutive_upper_case]
    return sum(spam_features) >= 2

