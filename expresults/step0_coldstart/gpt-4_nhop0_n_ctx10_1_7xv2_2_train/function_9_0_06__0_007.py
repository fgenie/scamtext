
import re

def is_spam(message):
    # Check for URL, numeric/percentage and non-consecutive capital letters
    url_pattern = r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\\(\\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+'
    numeric_percentage_pattern = r'\d+(?:\.\d+)?%?'
    capital_letters_pattern = r'[A-Z]{2,}'

    url_match = re.search(url_pattern, message)
    numeric_percentage_match = re.search(numeric_percentage_pattern, message)
    capital_letters_match = re.findall(capital_letters_pattern, message)

    # If there's a URL, numeric value, or percentage along with non-consecutive capital letters, classify it as spam
    if url_match and numeric_percentage_match and len(capital_letters_match) > 1:
        return True

    return False
