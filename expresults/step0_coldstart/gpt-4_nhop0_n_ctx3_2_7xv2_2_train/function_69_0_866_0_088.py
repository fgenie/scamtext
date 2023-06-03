
import re

def is_spam(message):
    # Check for common spam keywords
    keywords = ["추천주", "체험반", "정확한 분석", "검증된 수익률", "종목상담", "차별화된 정보"]
    contains_keyword = any(keyword in message for keyword in keywords)

    # Check for URL patterns
    url_pattern = re.compile(r'http\S+|www\.\S+|me2\.kr/\S+')
    has_url = url_pattern.search(message) is not None
    
    # Check for excessive use of special characters
    special_characters = ["*", "\"", "\n"]
    excessive_special_chars = sum(message.count(char) for char in special_characters) > 5

    return contains_keyword or has_url or excessive_special_chars
