
import re

def is_spam(text):
    # Customize regex patterns for spam patterns
    spam_patterns = [
        r'\d{2,}', # Strings with 2 or more consecutive numbers
        r'\d{1,}\%\s*상승', # Strings with percentage rise
        r'\d{1,}\%\s*출격', # Strings with percentage appearance
        r'http[s]?://.*', # Strings with URLs
        r'무료거부', # Strings with 'free refusal' (in Korean)
        r'\d{1,}[\.]\d{1,}', # Strings with floating point numbers
        r'\d+일장', # Numbers with '일장' ('일장' means 'stock')
        r'\b[A-Za-z.]+@[A-Za-z]+.[A-Za-z]+', # Email address
        r'[\(]\s*광고\s*[\)]', # Strings with advertisements ('광고' means 'advertisement' in Korean)
        r'(OCX|opx|OCP)', # Uncommon text patterns
    ]
    
    for pattern in spam_patterns:
        if re.search(pattern, text):
            return True
    return False
