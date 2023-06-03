
import re

def is_spam(message):
    # Check for presence of keywords, links and special punctuation
    keywords = ["VIP", "차별화", "추천", "목표달성", "휴대폰"]
    link_pattern = re.compile(r'https?://\S+')
    special_punctuation = re.compile(r'[\!\?]+')

    if any(keyword in message for keyword in keywords):
        return True
    if link_pattern.search(message):
        return True
    if special_punctuation.search(message):
        return True
    
    return False
