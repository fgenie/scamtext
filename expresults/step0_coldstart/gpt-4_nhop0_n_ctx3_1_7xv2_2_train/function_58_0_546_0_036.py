
import re

def contains_special_characters(text):
    if re.search('[^a-zA-Z0-9가-힣\s]', text):
        return True
    return False

def is_url(text):
    if re.search('http[s]?://(?:[a-zA-Z]|[0-9]|[.-]|[!*:\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', text):
        return True
    return False

def high_special_character_ratio(text):
    special_characters = sum([1 for char in text if not char.isalnum()])
    total_characters = len(text)
    return (special_characters / total_characters) > 0.25

def is_spam(text):
    if contains_special_characters(text) and is_url(text) and high_special_character_ratio(text):
        return True
    return False
