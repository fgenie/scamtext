
import re

def is_spam(message: str) -> bool:
    # Patterns frequently found in spam messages
    patterns = [
        r"\$[0-9,]+",  # Money amounts with commas and/or currency symbol
        r"http[^\s]+"  # URLs
    ]

    # Combine all patterns into a single regex pattern
    combined_pattern = "|".join(patterns)

    if re.search(combined_pattern, message) or len(message.split()) > 10:
        return True
    return False
