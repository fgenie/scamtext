
import re

def is_spam(text):
    # Check for URLs
    if re.search(r'(https?://[^\s]+)', text):
        return True

    # Check for phone numbers
    if re.search(r'(\+?\d[- .]?){7,13}', text):
        return True

    # Check for common spam phrases
    spam_phrases = [
        '무료수신거부', '상한가', '감사쿠폰', '특별찬스', '█+', '▲', '▼', '★+', '♥', '₩', 
        'VIP체험반', '㉿'
    ]
    for phrase in spam_phrases:
        if phrase in text:
            return True

    # Check for excessive use of special characters or capital letters
    special_chars = ['!', '@', '#', '$', '%', '&', '*', '(', ')', ',']
    count_special_chars = sum([1 for char in text if char in special_chars])
    count_capital_letters = sum([1 for char in text if char.isupper()])
    if count_special_chars >= 5 or count_capital_letters >= 10:
        return True

    return False
