
import re

def is_spam(message):
    # Lowercase the message
    message = message.lower()

    # Check for common spam keywords
    spam_keywords = ['해선', '성공지름길', '정확한 타점', '목표달성기념', '골드해선그룹', '비밀번호']
    for keyword in spam_keywords:
        if keyword in message:
            return True

    # Check for short urls
    short_urls = re.findall(r'(http|https)://([-\w.]+)+(\/[\w]{1,6})*', message)
    if len(short_urls) > 0:
        return True

    # Check for phone numbers like 0808783422
    phone_numbers = re.findall(r'01\d{8,9}', message) + re.findall(r'080\d{7}', message)
    if len(phone_numbers) > 1: 
        return True

    # If none of the above conditions apply, consider the message as normal
    return False
