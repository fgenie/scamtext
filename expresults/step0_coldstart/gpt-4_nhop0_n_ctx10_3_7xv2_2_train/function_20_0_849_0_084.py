
import re

def is_spam(message):
    
    # Patterns to detect spam messages
    spam_patterns = [
        r'\(광고\)',       # Spam in Korean language
        r'무료(거부|수신)',   # Free rejection or reception in Korean language
        r'080',           # Korean toll-free phone number starting with 080
        r'http(s)?://',   # URL presence
        r'(수익|적립|이벤트|특별|찬스|드립니다)', # Spammy keywords
        r'[\%\↑\↓]',      # Spammy characters
    ]
    
    # Combine all patterns into a single regular expression
    spam_pattern = re.compile('|'.join(spam_patterns), re.IGNORECASE)
    
    # Check if the message contains any of the spam patterns
    return bool(spam_pattern.search(message))
