
import re

def is_spam(message):
    spam_keywords = ["추천", "목표달성", "종목", "적중", "공개"]
    url_pattern = re.compile(r'(https?:\/\/(?:www\.|(?!www))[a-zA-Z0-9][a-zA-Z0-9-]+[a-zA-Z0-9]\.[^\s]{2,}|www\.[a-zA-Z0-9][a-zA-Z0-9-]+[a-zA-Z0-9]\.[^\s]{2,}|https?:\/\/(?:www\.|(?!www))[a-zA-Z0-9]+\.[^\s]{2,}|www\.[a-zA-Z0-9]+\.[^\s]{2,})')
    contains_url = bool(url_pattern.search(message))
    contains_keyword = any(keyword in message for keyword in spam_keywords)
    
    return contains_url and contains_keyword
