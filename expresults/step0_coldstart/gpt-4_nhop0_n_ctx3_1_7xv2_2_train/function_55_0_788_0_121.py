
import re

def is_spam(message):
    # Regular expressions to detect spam patterns
    url_pattern = re.compile(r'https?://(?:[-\w.]|(?:%[\da-fA-F]{2}))+')
    percentage_pattern = re.compile(r'\d{2,3}%')
    keywords = ['추천', '수익', '관망', '거래', '돈', '행복', '장기성', '단기', '안녕하세요', '리딩방', '비밀번호']

    # Check if message contains an URL
    if url_pattern.search(message):
        return True
        
    # Check if message contains percentage with 2 or 3 digits
    if percentage_pattern.search(message):
        return True
        
    # Check if message contains any spam keywords
    for keyword in keywords:
        if keyword in message:
            return True

    return False
