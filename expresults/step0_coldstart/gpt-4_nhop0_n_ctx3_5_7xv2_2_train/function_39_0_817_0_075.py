
import re

def is_spam(text):
    spam_keywords = ['광고', '수익', '상승', '무료거부', '안전하고 확률 높은 종목', 'fastkakao.com', 'me2.kr', 'han.gl']
    
    # Check for spam keywords
    for keyword in spam_keywords:
        if keyword in text:
            return True

    # Check for url, phone number and % character
    url_match = re.findall(r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\\(\\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', text)
    phone_match = re.findall(r'(\d{2,4})[-]?(\d{3,4})[-]?(\d{4})', text)
    percentage_match = re.findall(r'\d+%+', text)

    if url_match or phone_match or percentage_match:
        return True

    return False
