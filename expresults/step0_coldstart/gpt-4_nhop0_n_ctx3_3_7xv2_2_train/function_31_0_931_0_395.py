
import re

def is_spam(message):
    # Check for common spam words/patterns
    spam_words = ['(광고)', '카톡방', '입장', '안내', '상승', '히든종목', '아파트', '무료거부']
    spam_pattern = re.compile('|'.join(spam_words))
    
    # Check for url patterns
    url_pattern = re.compile(r'https?://[^\s]+')
    
    # Check for special characters or large spaces
    special_char_pattern = re.compile(r'[\W]{2,}')
      
    if spam_pattern.search(message) or url_pattern.search(message) or special_char_pattern.search(message):
        return True
    else:
        return False
