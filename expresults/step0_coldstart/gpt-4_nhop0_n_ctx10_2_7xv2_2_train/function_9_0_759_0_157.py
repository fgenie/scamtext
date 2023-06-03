
import re

def is_spam(message):
    # Check for URL patterns
    urls = re.findall(r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\\(\\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', message)
    short_urls = re.findall(r'bit\.ly/\S+|me2\.kr/\S+|han\.gl/\S+|kakaosa\.co\.kr|openkakao\.(?:at|com)/\S+', message)

    # Check for excessive capitalization
    caps_ratio = sum(1 for c in message if c.isupper()) / len(message)
    
    # Check for excessive special characters
    special_chars = re.findall(r'[!?.*#]+', message)
    special_chars_ratio = len(special_chars) / len(message)

    # Check for keyword patterns related to spam
    keywords = re.findall(r'이벤트|상한가|증권|공시|매수|추천종목|방법|공개|벌써|달성|{}|%|주식', message)
    
    # Check conditions (adjust thresholds if needed)
    if len(urls) > 0 or len(short_urls) > 0 or caps_ratio > 0.3 or special_chars_ratio > 0.1 or len(keywords) >= 3:
        return True
    else:
        return False
