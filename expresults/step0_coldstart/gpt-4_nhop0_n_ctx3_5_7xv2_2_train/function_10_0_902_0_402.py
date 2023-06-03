
import re

def is_spam(text):
    # Check for unusual characters and signs
    unusual_chars = ['▼', '▲']
    for char in unusual_chars:
        if char in text:
            return True

    # Check for urls that may be spam
    spam_url_patterns = ['me2\.kr', 'ktalk\.org', 'kakaos\.co', 'buly\.kr']
    for pattern in spam_url_patterns:
        if re.findall(pattern, text):
            return True

    # Check for unusually high percentage of numbers and special characters
    non_alphabetic_chars = re.findall('[^a-zA-Z가-힣]', text)
    non_alphabetic_ratio = len(non_alphabetic_chars) / len(text)
    if non_alphabetic_ratio > 0.3:
        return True

    # Check for keywords related to spam: VIP, 시크릿, 필승전략, 이벤트, 돈, etc.
    spam_keywords = ['VIP', '시크릿', '필승전략', '이벤트', '돈']
    for keyword in spam_keywords:
        if keyword in text:
            return True

    return False
