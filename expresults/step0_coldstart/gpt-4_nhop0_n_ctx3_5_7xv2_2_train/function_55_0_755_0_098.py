
import re

def is_spam(message: str) -> bool:
    # Check for common spam message patterns
    patterns = [
        r'https://me2\.kr/\w+',    # Shortened URLs
        r'\+',                     # Plus signs
        r'\d{1,3}\.?\d{0,3}\,?\d{3}', # Money amounts
        r'bit\.ly/\w+',            # Bitly links
        r'\b(광고)\b',              # Korean word for 'advertisement'
        r'\b코드\s*:\s*\d{4}\b',    # Code followed by 4 digit number
        r'KRW',                    # Currency abbreviation
        r'무료거부\s*\d{10}',       # Korean phrase for 'free reject' followed by 10 digit number
    ]
    for pattern in patterns:
        if re.search(pattern, message):
            return True
    return False
