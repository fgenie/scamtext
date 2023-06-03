
import re

def is_spam(text):
    spam_patterns = [
        r"https?:\/\/me2\.kr", # Specific spam URL patterns
        r"VIP",
        r"\d+%",
        r"{\S}?[\w|\S]{2,}\S+[\/|\(|\[]", # Suspicious sequences of characters and symbols
        r"\d{1,3}[,\s]\d{3}원" # Amounts in Korean currency format
    ]
    
    if any(re.search(pattern, text) for pattern in spam_patterns):
        return True
    return False
