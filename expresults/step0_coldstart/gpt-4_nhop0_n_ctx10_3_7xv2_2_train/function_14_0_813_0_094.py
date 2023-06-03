
import re

def is_spam(message):
    # Patterns for detecting spam
    url_pattern = re.compile(r'https?://\S+')
    number_pattern = re.compile(r'\d{4,}')
    repeated_pattern = re.compile(r'(\S+)(\s+\1)+')
    ads_pattern = re.compile(r'\b(광고)\b', re.IGNORECASE)
    consecutive_uppercase_pattern = re.compile(r'([A-Z]){3,}')

    # Check for patterns in the message
    url_detected = bool(url_pattern.search(message))
    number_detected = bool(number_pattern.search(message))
    repeated_detected = bool(repeated_pattern.search(message))
    ads_detected = bool(ads_pattern.search(message))
    consecutive_uppercase_detected = bool(consecutive_uppercase_pattern.search(message))

    # If any of the patterns are detected, the message is considered spam
    return url_detected or number_detected or repeated_detected or ads_detected or consecutive_uppercase_detected
