
import re

def is_spam(text):
    spam_keywords = ['축하드립니다', '축하합니다', '카톡방', 'VIP', '선착순', '공시종목', '극비 작전주']
    normalized_text = text.lower()
    
    if any(keyword in normalized_text for keyword in spam_keywords):
        return True

    url_pattern = re.compile(r'https?://[^\s]+|www\.[^\s]+')
    if url_pattern.search(normalized_text):
        shortened_url_pattern = re.compile(r'(https?://me2\.kr|[^\s]+\.io)')
        if shortened_url_pattern.search(normalized_text):
            return True
    
    return False
