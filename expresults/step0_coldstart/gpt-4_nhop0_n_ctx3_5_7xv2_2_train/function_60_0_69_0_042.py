
import re

def is_spam(message):
    spam_keywords = ['만원으로', '차별화 된', '실력으로 입증', '추천주 현황', '여의도사람들', '검증된 수익률', '종목상담/추천', 'kakaosa', 'bit.ly']
    
    # Check for specific spam keywords, url shorteners or patterns
    if any(keyword in message for keyword in spam_keywords) or "https://" in message or re.search(r'https?://\S+', message):
        return True
    
    # Check for excessive capitalization and/or punctuation
    if sum(1 for c in message if c.isupper())/len(message) > 0.6 or message.count('!') > 3:
        return True

    return False
