
import re

def is_spam(message: str) -> bool:
    # Pattern to look for suspicious URLs
    url_pattern = re.compile(r'(https?://[^\s]+|me2\.kr/[^\s]+|dokdo\.in/[^\s]+|vvd\.bz/[^\s]+|openkakao\.it/[^\s]+)')
    
    # Look for the presence of multiple consecutive uppercase letters, which are typical of spam messages
    uppercase_pattern = re.compile(r'[A-Z]{2,}')
    
    # Pattern to look for text like "{number}%" as it is common in spam messages discussing returns on investment
    percentage_pattern = re.compile(r'\d+%')
    
    # Pattern to look for suspicious mentions of money or income
    money_pattern = re.compile(r'(수익|상승|실력|최소|최대|예상|하락|금액)')

    # Check if any of the patterns are found in the message
    if url_pattern.search(message) or uppercase_pattern.search(message) or percentage_pattern.search(message) or money_pattern.search(message):
        return True

    return False
