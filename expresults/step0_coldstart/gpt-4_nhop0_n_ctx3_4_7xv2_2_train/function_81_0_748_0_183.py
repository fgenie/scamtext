
import re

def is_spam(message):
    # Checking for common spam keywords
    spam_keywords = ["단타정보트레이딩", "(광고)", "무료종목", "참고로", "원칙", "이점", "명심", "지속 정보를 희망", "관심종목", "상승가능성", "무료거부"]
    
    # Convert message to lowercase
    message = message.lower()
    
    # Check presence of spam keywords in message
    for keyword in spam_keywords:
        if keyword in message:
            return True
    
    # Check if message has multiple consecutive special characters
    if re.search(r"[\!\"#\$%&\(\)\*\+,\-./:;<=>\?@\[\\\]\^_`{\|}~]{2,}", message):
        return True
    
    # Check if message has multiple consecutive upper case words of length more than 1
    if len(re.findall(r"\b[A-Z][A-Z]+\b", message)) > 1:
        return True
    
    return False
