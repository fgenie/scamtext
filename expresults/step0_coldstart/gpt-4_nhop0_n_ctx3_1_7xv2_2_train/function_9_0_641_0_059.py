
import re

def is_spam(text):
    # Keywords commonly found in spam messages
    spam_keywords = ['루징', '억보증', '추천주', '성공지름길', '정확한 타점', '탈출나스놉', '루징', '요율']
    
    # Regular expressions to identify suspicious URLs and phone numbers
    url_pattern = re.compile(r'(http|https)://[^\s]*')
    phone_pattern = re.compile(r'\d{2,4}-\d{3,4}-\d{4}')

    # Check if the text contains any spam keywords
    if any(keyword in text for keyword in spam_keywords):
        return True

    # Check if the text contains suspicious URLs
    urls = url_pattern.findall(text)
    if len(urls) > 0:
        return True

    # Check if the text contains phone numbers
    phones = phone_pattern.findall(text)
    if len(phones) > 0:
        return True

    return False
