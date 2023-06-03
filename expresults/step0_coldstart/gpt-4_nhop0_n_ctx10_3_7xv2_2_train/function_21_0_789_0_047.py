
import re

def is_spam(message):
    # Checking for spam patterns
    spam_patterns = [
        r'\d+%(?!\d)',  # Number followed by %
        r'https?:\/\/[^\s]*',  # URLs
        r'(?!www\.)\W{3,}\.[^\s]*',  # Shortened URLs
        r'[A-Za-z0-9]+@[A-Za-z0-9]+\.[A-Za-z]+',  # Email addresses
        r'(?i)(광고)', # Advertisement keyword
        r'\b혜택\b',  # '혜택' keyword
        r'\b지원금\b',  # '지원금' keyword
        r'(?i)(코드)[:("\s]*\d+',  # '코드' followed by numbers
        r'%\+BBQ|BBQ\+%']  # String combination of '+' , '%' and 'BBQ'

    for pattern in spam_patterns:
        if re.search(pattern, message):
            return True

    return False

