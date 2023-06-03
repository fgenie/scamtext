
import re

def is_spam(message: str) -> bool:
    # Rule 1: Check for common spam keywords like "광고", "무료", "지급", "입장코드"
    spam_keywords = ["광고", "무료", "지급", "입장코드"]
    if any(keyword in message for keyword in spam_keywords):
        return True

    # Rule 2: Check for a sequence of two or more capitalized words
    if re.search(r'([가-힣A-Za-z]{2,}\s){2,}', message):
        return True

    # Rule 3: Check for unusual URLs
    unusual_urls = ["bit.ly", "me2.kr"]
    if any(url in message for url in unusual_urls):
        return True

    # Rule 4: Check for sequences of numbers
    if re.search(r'\d{3,}', message):
        return True

    # Rule 5: Check for message with a very high count of special characters
    special_chars = re.findall(r'[!@#$%^&*()_+={}\[\]:";<>?\\/|.]+', message)
    if len(special_chars) > 5:
        return True
        
    return False
