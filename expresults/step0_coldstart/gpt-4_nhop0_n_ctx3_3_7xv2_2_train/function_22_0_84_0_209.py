
import re


def is_spam(message):
    # Check for common spam patterns in the message
    patterns = [
        r'https?:\/\/\S+',  # URL
        r'\b[0-9]{1,}\b',   # Numbers
        r'bit\.ly\/\S+',     # Shortened URL
        r'\b[-!@#$%^&*()_+]*',  # Special characters (not used in words)
        r'[ㄱ-ㅎㅏ-ㅣ]++',  # A sequence of Korean characters.
        r'\\u[\dA-Fa-f]+',  # Unicode escape codes
        r'\d{2,}[,.]\d{2,}',  # Large, decimal-like numbers
    ]
    
    found = [re.search(pattern, message, re.IGNORECASE) for pattern in patterns]

    # If more than one pattern is found in the message, it is likely to be spam
    return sum(bool(match) for match in found) >= 2

