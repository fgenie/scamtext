
import re

def is_spam(message):
    # Check for presence of URL
    url_pattern = re.compile(r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\\(\\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+')
    contains_url = bool(url_pattern.search(message))

    # Check for presence of stock symbols, e.g. (038060) or (060230)
    stock_pattern = re.compile(r'\([0-9]{6}\)')
    contains_stock = bool(stock_pattern.search(message))

    # Check for presence of special characters, e.g. ! or %
    special_characters_pattern = re.compile(r'[!%]')
    contains_special_characters = bool(special_characters_pattern.search(message))

    # Check for presence of words like "추천", "적중"
    spam_words = ["추천", "적중"]
    contains_spam_words = any(word in message for word in spam_words)

    return contains_url and (contains_stock or contains_special_characters or contains_spam_words)
