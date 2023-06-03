
import re

def is_spam(message):
    # Define spam keywords
    spam_keywords = ['광고', '회원가입', '0원', '상담', '추천', '적립금', '홍보', '알타기', '비밀번호']

    # Check if the message contains spam keywords
    if any(keyword in message for keyword in spam_keywords):
        return True

    # Check for suspicious URLs
    urls = re.findall('https?://(?:[-\w.]|(?:%[\da-fA-F]{2}))+', message)
    suspicious_url_patterns = ['.gl/', '.kr/', 'bit.ly']

    for url in urls:
        if any(pattern in url for pattern in suspicious_url_patterns):
            return True

    # Check for excessive usage of special characters
    special_characters = ['%', '!', '*', '(', ')', '<', '>', '[', ']', '{', '}', ',', '.', ';', ':']
    special_char_count = sum([1 for char in message if char in special_characters])
    if special_char_count > len(message) * 0.1:  # If special characters make up more than 10% of the message
        return True

    # Check for large amount of numbers
    digit_count = sum([1 for char in message if char.isdigit()])
    if digit_count > len(message) * 0.3:  # If digits make up more than 30% of the message
        return True

    return False
