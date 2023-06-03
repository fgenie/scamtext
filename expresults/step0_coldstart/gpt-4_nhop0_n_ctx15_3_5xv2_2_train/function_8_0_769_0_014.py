
import re

def is_spam(message: str) -> bool:
    # Check for typical spam patterns related to money and URLs
    money_keywords = ['만원', '백만원', '신속', '지원금', '할인', '혜택', '마감']
    spam_url_pattern = re.compile(r'(https?:\/\/\S*[정보투자]|\S*(bit\.ly|me2\.kr|asq\.kr|openkakao)\S*)')
    
    if any(keyword in message for keyword in money_keywords) or re.search(spam_url_pattern, message):
        return True
    
    # Check for advertisement tag in the message
    if "(광고)" in message:
        return True

    return False
