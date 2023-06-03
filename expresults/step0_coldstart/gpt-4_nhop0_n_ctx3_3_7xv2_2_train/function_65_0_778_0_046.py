
import re

def is_spam(text):
    # Check for spam patterns
    spam_patterns = [
        r"\d%[가-힣]+\d%",  # Percentage with Korean texts
        r"http[s]?://",  # URLs
        r"bit.ly",  # Shortened URLs
        r"code:",  # Codes
        r"톡\w+",  # 카톡 IDs
        r"▼",  # Special characters
        r"\(광고\)",  # Advertising indication
        r"무료거부",  # Opt-out messages
        r"무료문자수신거부"  # Opt-out messages
    ]
    
    # Iterate through spam_patterns and check if they exist in the input text
    for pattern in spam_patterns:
        if re.search(pattern, text, re.IGNORECASE):
            return True
    
    # Return False if no spam_patterns were found
    return False
