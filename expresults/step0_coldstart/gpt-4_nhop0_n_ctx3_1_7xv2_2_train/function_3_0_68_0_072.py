
import re

def is_spam(message):
    patterns = [
        # URL pattern
        r"((https?):\/\/\S+(\.([A-Za-z]{2,}))\/\S*)",
        
        # Number of consecutive special characters, such as "%", "▲", "▼"
        r"([\%\!\?\^\*_\-]{3,})",
        
        # Repeated capitalization (uppercase) with or without numbers
        r"((\b[A-Z0-9]+\b\s*){2,})",
    ]

    for pattern in patterns:
        if re.search(pattern, message):
            return True

    return False
