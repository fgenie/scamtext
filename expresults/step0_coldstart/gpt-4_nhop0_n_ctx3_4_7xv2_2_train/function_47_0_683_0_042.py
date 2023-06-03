
import re

def is_spam(message):
    spam_indicators = [
        r'.*(\$|웃|[원])\s+([0-9]){4,}\s+(\$|웃|[원])', # patterns like 10000$ or 만원
        r'.*(\.|\s)([a-z]){7,}\s*(\.|\s)+', # sequences of 7 or more lowercase letters
        r'http.?://.{3,}\.[A-Za-z]{2,3}(/\w+)?' # URLs
    ]
    
    for indicator in spam_indicators:
        if re.search(indicator, message):
            return True
    return False
