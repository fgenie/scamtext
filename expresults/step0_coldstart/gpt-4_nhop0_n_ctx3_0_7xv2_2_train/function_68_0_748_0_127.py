
import re

def is_spam(message):
    # Check for spam-related keywords
    spam_keywords = ['vip', '비공개', '대형공시', '필요한 핵심', '목표가', '폭등예상', '수익']
    for keyword in spam_keywords:
        if keyword in message.lower():
            return True

    # Check for unusual URL patterns
    url_pattern = re.compile(r'(https?:\/\/\S+)')
    urls = re.findall(url_pattern, message)
    for url in urls:
        if 'me2' in url or 'opcn' in url:
            return True

    # Check for excessive special characters
    special_chars = ['/', '\\', '!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '+', '=', '[', ']', '{', '}', ':', ';', ',', '.', '<', '>', '|']
    char_count = sum([message.count(char) for char in special_chars])
    if char_count / len(message) > 0.1:
        return True
    
    return False
