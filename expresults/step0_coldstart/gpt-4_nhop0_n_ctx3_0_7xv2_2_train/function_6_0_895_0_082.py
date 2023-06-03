
import re

def is_spam(text):
    # Check for typical spam characteristics
    spam_indicators = [
        r"(?i)\b(광고|올|퍼.센|다.in|달성|참.차|인.증|메쎄)\b", # Common spam phrases
        r"\d{2}[%퍼.센]", # Numbers followed by a percent sign
        r"\b[a-zA-Z0-9]+\.[a-zA-Z]{2,}\b", # URLs with a TLD
        r"[0-9]{4}([ -.]?)[0-9]{2}([ -.]?)[0-9]{2}", # Dates in various formats
        r"무료수신거부", # Unsubscribe text
    ]

    # Loop through spam indicators and check for matches
    for indicator in spam_indicators:
        if re.search(indicator, text):
            return True

    return False
