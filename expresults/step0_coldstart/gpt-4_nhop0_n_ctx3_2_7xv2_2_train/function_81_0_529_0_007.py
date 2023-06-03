
import re

def contains_korean(text):
    return bool(re.search(r'[\uAC00-\uD7A3]', text))

def contains_url(text):
    return bool(re.search(r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\\(\\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', text))

def high_linebreak_ratio(text, threshold=0.05):
    return text.count('\n') / len(text) > threshold

def is_spam(text):
    if contains_korean(text) and contains_url(text) and high_linebreak_ratio(text):
        return True
    return False
