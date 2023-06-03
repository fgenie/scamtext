
import re


def is_spam(text):
    # Spam patterns
    spam_patterns = [
        r"http\S+",                     # URLs
        r"\d{2}%|평균|분석|추천",          # Profits, percentages, analysis or recommendations
        r"(?i)(vip|대공개|디젠스|비법)",  # Case-insensitive keywords
    ]
    
    # Replace newline characters with a space
    text = text.replace("\n", " ")
    
    for pattern in spam_patterns:
        if re.search(pattern, text):
            return True
    
    return False
