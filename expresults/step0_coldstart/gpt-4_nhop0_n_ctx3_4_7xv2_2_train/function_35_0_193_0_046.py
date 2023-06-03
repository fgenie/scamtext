
import re

def is_spam(text):
    if not text:
        return False

    # Check for (광고) keyword at the beginning
    if text.startswith('(광고)'):
        return True
    
    # Check for multiple short urls
    urls = re.findall(r'(https?://\S+)', text)
    if len(urls) > 1:
        return True

    # Check for 거부(무료), 무료거부, or (선착) keywords
    if '거부(무료)' in text or '무료거부' in text or '(선착)' in text:
        return True

    # Check for 숫자(serial numbers)
    digits = re.findall(r'\d{4,}', text)
    if len(digits) > 1:
        return True
    
    # Check for suspicious money amounts
    amounts = re.findall(r'[\d,]+원', text)
    if len(amounts) > 2:
        return True

    return False
