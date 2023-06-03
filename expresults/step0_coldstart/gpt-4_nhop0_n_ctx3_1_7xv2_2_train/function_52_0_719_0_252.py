
import re

def is_spam(text):
    # Lowercase the text for case-insensitive analysis
    text_lower = text.lower()

    # Check for some common spam phrases
    spam_phrases = ["금일 하루만", "광고", "빠르고 정확한", "입장코드", "무료거부"]

    for phrase in spam_phrases:
        if phrase in text_lower:
            return True

    # Check for a higher number of special characters
    special_characters = "!?*%$"
    special_count = sum(1 for char in text if char in special_characters)
    if special_count > len(text) * 0.05:
        return True

    # Check for URLs
    url_pattern = re.compile(r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+')
    if url_pattern.search(text):
        return True

    # Check for a higher number of non-alphanumeric characters
    non_alnum_count = sum(1 for char in text if not char.isalnum() and not char.isspace())
    if non_alnum_count > len(text) * 0.3:
        return True

    # If none of the above conditions are met, it's likely not a spam message
    return False
