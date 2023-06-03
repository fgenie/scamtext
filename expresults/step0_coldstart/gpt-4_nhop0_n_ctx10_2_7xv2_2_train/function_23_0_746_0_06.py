
import re

def is_spam(text):
    # Check for spam keywords
    spam_keywords = ["상승", "대응", "상한", "매수", "매도", "분석", "수익률", "관리자", "신규", "공시", "체험반", "추천"]
    for keyword in spam_keywords:
        if keyword in text:
            return True
    
    # Check for URL patterns
    url_pattern = r'(https?:\/\/(?:www\.|(?!www))[a-zA-Z0-9][a-zA-Z0-9-]+[a-zA-Z0-9]\.[^\s]{2,}|www\.[a-zA-Z0-9][a-zA-Z0-9-]+[a-zA-Z0-9]\.[^\s]{2,}|https?:\/\/(?:www\.|(?!www))[a-zA-Z0-9]+\.[^\s]{2,}|www\.[a-zA-Z0-9]+\.[^\s]{2,})'
    urls = re.findall(url_pattern, text)
    if len(urls) > 0:
        return True

    # Check for repeating characters/words
    repeating_characters = re.findall(r'(\w)\1{3,}', text)
    if len(repeating_characters) > 0:
        return True
    
    return False
