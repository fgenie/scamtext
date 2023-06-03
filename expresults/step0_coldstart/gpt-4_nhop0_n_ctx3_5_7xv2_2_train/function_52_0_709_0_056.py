
import re

def is_spam(message):
    # Keywords that may appear in spam messages
    spam_keywords = ['광고', '수익 보장', '다름이 아니라', '주식계좌', '원의 비용요구', '선착순', '무료거부']

    # Patterns that may appear in spam messages
    spam_patterns = [
        r'https?://\S+',  # URLs
        r'\d{3}\w\d{3}\w\d{3}'  # Phone numbers like 0803705780
    ]

    # Checking if any keyword is in the message
    if any(keyword in message for keyword in spam_keywords):
        return True

    # Checking if any spam pattern is in the message
    if any(re.search(pattern, message) for pattern in spam_patterns):
        return True
    
    return False
