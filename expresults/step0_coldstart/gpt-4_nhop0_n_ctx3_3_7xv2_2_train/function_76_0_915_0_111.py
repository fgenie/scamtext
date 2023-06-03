
import re

def is_spam(message: str) -> bool:
    # Check for excessive use of special characters
    special_chars = re.findall(r'[\\*>~&]+', message)
    if len(special_chars) > 1:
        return True

    # Check for URL shorteners or suspicious links
    suspicious_urls = re.findall(r'https?://\S+|me2\.kr|bit\.ly|ko\.gl|\.\.kr', message)
    if suspicious_urls:
        return True

    # Check for unrealistic claims, such as large amounts of money or government support
    unrealistic_claims = re.findall(r'\d{2,},\d{3,}|정부 \d{2,}조지원', message)
    if unrealistic_claims:
        return True

    # Check for non-Korean characters, which might indicate a foreign spam source
    non_korean_chars = re.findall(r'[^\가-힣\s\.,\'"()\/:;?!“”‘’–—―\[\]]', message)
    if len(non_korean_chars) > 5:
        return True
        
    return False
