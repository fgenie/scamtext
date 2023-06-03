
import re

def is_spam(message):
    # Check for presence of numbers or special characters
    if re.search(r'\d', message) or re.search(r'[^\w\s]', message):
        # Check for presence of URL
        if re.search(r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\\(\\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', message):
            return True
        
        # Check for presence of short URL
        if re.search(r'bit\.ly|goo\.gl|me2\.kr|tinyurl\.com|ocx\.kr|buly\.kr', message):
            return True

        # Check for promotional keywords
        promotional_keywords = ['광고', '프로모션', '이벤트', '쿠폰', '할인', '구인', '회원가입', '신규', '주식', '공시', '정보', '단독', '상한가', '경품']
        for keyword in promotional_keywords:
            if keyword in message:
                return True
     
    return False
