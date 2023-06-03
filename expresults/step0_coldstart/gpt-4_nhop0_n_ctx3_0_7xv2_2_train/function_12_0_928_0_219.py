
import re

def is_spam(message):
    # Check for unusual URL patterns
    url_patterns = [r"(?i)\b((?:https?://|www\d{0,3}[.]|[a-z0-9.\-]+[.][a-z]{2,4}/)(?:[^\s()<>]+|\(([^\s()<>]+|(\([^\s()<>]+\)))*\))+(?:\(([^\s()<>]+|(\([^\s()<>]+\)))*\)|[^\s`!()\[\]{};:'\".,<>?«»“”‘’]))", 
                    r"openkakao\.[a-z]+/[a-zA-Z0-9]+"]

    # Check for excessive use of special characters
    special_char_pattern = r"[^\w\s?!.,;@가-힣]+"

    # Check for large numbers (more than 4 digits)
    large_number_pattern = r"\d{5,}"

    # Check for repetitive characters
    repetitive_char_pattern = r"(.)\1{2,}"

    patterns = [url_patterns, special_char_pattern, large_number_pattern, repetitive_char_pattern]

    for pattern in patterns:
        if isinstance(pattern, list):
            for sub_pattern in pattern:
                if re.search(sub_pattern, message):
                    return True
        else:
            if re.search(pattern, message):
                return True

    return False
