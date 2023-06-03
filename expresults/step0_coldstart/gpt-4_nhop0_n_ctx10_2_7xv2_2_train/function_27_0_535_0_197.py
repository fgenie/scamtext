
import re

def has_url(text):
    regex = r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\\(\\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+'
    return bool(re.search(regex, text))

def has_digit_words(text):
    regex = r'\d{1,}[a-zA-Z가-힣]{1,}'
    return bool(re.search(regex, text))

def has_percentage(text):
    regex = r'\d{1,}%'
    return bool(re.search(regex, text))

def has_currency(text):
    regex = r'\d{1,}[\,\.]{0,}\d{0,}원'
    return bool(re.search(regex, text))

def too_many_special_chars(text):
    special_chars_ratio = sum(char in "!#$%&'*+-.:=?@[]^_`{|}~" for char in text) / len(text)
    return special_chars_ratio > 0.1

def is_spam(text):
    if has_url(text) and (has_digit_words(text) or has_percentage(text) or has_currency(text)):
        return True

    if too_many_special_chars(text):
        return True

    return False
