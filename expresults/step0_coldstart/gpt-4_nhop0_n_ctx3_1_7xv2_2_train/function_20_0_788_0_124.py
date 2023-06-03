
import re

def is_spam(text):
    # Check for consecutive uppercase words, suggestive of spam
    uppercase_pattern = r'\b[A-Z]{2,}\b'
    if re.search(uppercase_pattern, text):
        return True

    # Check for an excessive number of symbols, suggesting a spam link
    symbols_pattern = r"[!%&/()@_*()[]]"
    symbols_count = len(re.findall(symbols_pattern, text))
    if symbols_count >= 3:
        return True

    # Check for words suggestive of spam content
    spam_keywords = ["추천", "↑", "https", "님"]
    if any(keyword in text for keyword in spam_keywords):
        return True

    # Ensure the message isn't an advertisement rather than spam
    advertisement_check = "(광고)"
    if advertisement_check in text:
        return False

    return False
