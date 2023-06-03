
import re

def is_spam(message: str) -> bool:
    # URL patterns containing shortening services
    short_url_regex = re.compile(r'(http|https)://(bit\.ly|me2\.kr|gg\.gg|buly\.kr|t\.co|goo\.gl|tinyurl\.com|tr\.im)/\S+')
    
    # Special non-alphanumeric characters
    non_alphanumeric_regex = re.compile(r'[.,?^+\-%\*/:]+')

    # Matching common phrases in spam messages
    spam_phrases = ['VIP', '급등', '종목']

    url_count = len(short_url_regex.findall(message))
    non_alphanumeric_count = len(non_alphanumeric_regex.findall(message))
    phrase_count = sum(1 for phrase in spam_phrases if phrase in message)
    
    if url_count >= 1 and (non_alphanumeric_count >= 2 or phrase_count >= 1):
        return True

    return False
