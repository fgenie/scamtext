
import re

def is_spam(message):
    
    # Checking for spam keywords in the message
    spam_keywords = ['추천주', '수익률', '️꽁머', '차익방', '배워보', '사다리', '배터', '단속', '천지일보', '정보공유']

    if any(keyword in message for keyword in spam_keywords):
        return True

    # Checking for suspicious links
    url_pattern = re.compile(r'https?://[^\s]+')
    urls = re.findall(url_pattern, message)

    if urls:
        spam_domain_pattern = re.compile(r'\.(kr|me2|dokdo|han)')
        for url in urls:
            if re.search(spam_domain_pattern, url):
                return True

    # Checking for excessive use of special characters
    special_characters = ['↑', '★', '▼', '️']

    if any(char in message for char in special_characters):
        return True

    # No spam detected
    return False
