
import re

def contains_number(text):
    return bool(re.search(r'\d', text))

def contains_url(text):
    return bool(re.search(r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\\(\\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', text))

def contains_bitly(text):
    return bool(re.search(r'bit\.ly', text))

def contains_currency_symbol(text):
    return bool(re.search(r'[₩$€£¥₹₽]', text))

def excessive_punctuation(text):
    return bool(re.search(r'[\?!]{2,}', text))

def has_obscure_characters(text):
    return bool(re.search(r"[^a-zA-Z0-9\s。，！？、；！\.,?!'\"]", text))

def is_spam(text):
    text = text.lower()
    if contains_number(text) and contains_url(text) and contains_currency_symbol(text):
        return True
    if contains_bitly(text) and contains_url(text):
        return True
    if excessive_punctuation(text):
        return True
    if has_obscure_characters(text):
        return True

    return False
