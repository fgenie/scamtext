
import re

def is_spam(message):
    # Check for common spam keywords
    spam_keywords = ['적중', '상한가', '투자', '최대', '할인', '광고', '증시', '최고급', '상승', '거래량', '상승확정']
    
    # Check for excessive use of special characters
    special_chars_pattern = re.compile(r'[^a-zA-Z0-9가-힣.\s]+')
    special_chars_count = len(special_chars_pattern.findall(message))

    # Check for url shorteners
    url_shorteners_pattern = re.compile(r'(me2\.kr|vo\.la|vvd\.bz|오픈톡\.com|openkakao\.[a-z]+)')
    url_shorteners_count = len(url_shorteners_pattern.findall(message))

    # Check for phone numbers
    phone_pattern = re.compile(r'\d{2,4}-\d{3,4}-\d{4}')
    phone_count = len(phone_pattern.findall(message))

    # Classify as spam if message contains any spam keywords, multiple instances of special characters, url shorteners or phone numbers
    if any(keyword in message for keyword in spam_keywords) or special_chars_count > 2 or url_shorteners_count > 0 or phone_count > 0:
        return True

    return False
