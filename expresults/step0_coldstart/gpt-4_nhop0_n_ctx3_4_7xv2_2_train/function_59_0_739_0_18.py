
import re

def is_spam(message: str) -> bool:
    # Spam characteristics
    url_pattern = re.compile(r'https?://\S+')
    special_chars_pattern = re.compile(r'[^\w\s,]') 
    excessive_whitespace = re.compile(r'\s{2,}')
    excessive_newlines = re.compile(r'\n{2,}')

    # Count the percentage of special characters in the message
    special_chars_ratio = len(special_chars_pattern.findall(message)) / len(message)

    # Check if there are URLs, excessive whitespaces or newlines in the message
    has_url = bool(url_pattern.search(message))
    has_excessive_whitespace = bool(excessive_whitespace.search(message))
    has_excessive_newlines = bool(excessive_newlines.search(message))

    # Check if the message contains stock or investing related words
    stock_related_words = ['투자', '매수', '매도', '종목', '상장', '체험']
    contains_stock_words = any(word in message for word in stock_related_words)

    # Classify as spam if:
    # 1. The message has URL and contains stock-related words
    # 2. The message has excessive whitespaces or newlines
    # 3. The special characters ratio is higher than 20%
    if has_url and contains_stock_words:
        return True
    elif has_excessive_whitespace or has_excessive_newlines:
        return True
    elif special_chars_ratio > 0.20:
        return True

    return False
