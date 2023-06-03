
import re

def is_spam(message):
    # Use regex to check for patterns associated with spam messages
    # 1. Multiple special characters
    pattern_1 = re.compile(r'(?:(?:[_!$%^&*@#]+){3,})')
    
    # 2. URLs with unusual patterns
    pattern_2 = re.compile(r'https?://\S{5,}\.k[rz]{1}.*')

    # 3. Checking for increase in prices
    pattern_3 = re.compile(r'\d+(?:\.\d+)?원\s?.+\s?\d+(?:\.\d+)?원')

    # 4. Checking for excessive use of punctuation or line breaks
    pattern_4 = re.compile(r'[-|=]{3,}|(\n\s*){3,}')

    if pattern_1.search(message) or pattern_2.search(message) or pattern_3.search(message) or pattern_4.search(message):
        return True
    else:
        return False
