
import re

def is_spam(message):
    # Check for suspicious strings, exclamation marks, or all-uppercase words
    spam_terms = ['클릭', '알려드립니다', '축하합니다', '▼', '▲', '※', '무료입장', '누적수익률']
    for term in spam_terms:
        if term in message:
            return True
    
    # Check for URLs with suspicious domains
    urls_pattern = re.compile(r'https?://(?:[^\s/]*\.)?(?:me2|openkakao)\.([a-zA-Z0-9]){2}')
    if urls_pattern.search(message):
        return True
    
    # Check for overusing special characters
    if sum(c.isdigit() for c in message) / len(message) > 0.1:
        return True

    return False
