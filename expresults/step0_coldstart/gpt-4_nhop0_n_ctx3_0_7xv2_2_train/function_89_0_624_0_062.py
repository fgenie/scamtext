
import re

def contains_url(text):
    url_pattern = re.compile(r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\\(\\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+')
    return bool(url_pattern.search(text))

def excessive_punctuation(text):
    excessive_punctuation_patterns = [
        re.compile(r'\.{3,}'),
        re.compile(r'\?{3,}'),
        re.compile(r'!{3,}'),
    ]
    for pattern in excessive_punctuation_patterns:
        if pattern.search(text):
            return True
    return False

def is_spam(text):
    features = [
        contains_url(text),
        excessive_punctuation(text),
    ]
    return any(features)

