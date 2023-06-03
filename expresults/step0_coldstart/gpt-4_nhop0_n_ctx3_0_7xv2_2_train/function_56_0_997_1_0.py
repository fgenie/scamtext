import re

def is_spam(message):
    # Patterns to detect:
    # 1. Presence of URLs
    url_pattern = re.compile(r'(https?://|www\d{0,3}\.|[a-z0-9.-]+\.[a-z]{2,4}/)[^\s]*')

    # 2. Presence of numbers followed by special characters and percentages
    number_special_char_pattern = re.compile(r'\d+[\%\)\(\"\'\^]+')

    # 3. Presence of non-unicode characters
    non_unicode_pattern = re.compile(r'[^\x00-\x7F]+')

    # 4. Presence of too many uppercase letters
    uppercase_pattern = re.compile(r'[A-Z]{3,}')

    # 5. Presence of free offers, 문자열 광고의 존재
    free_offer_pattern = re.compile(r'(무료|광고|성과)')

    if (url_pattern.search(message) or
        number_special_char_pattern.search(message) or
        non_unicode_pattern.search(message) or
        uppercase_pattern.search(message) or
        free_offer_pattern.search(message)):
        return True
    else:
        return False