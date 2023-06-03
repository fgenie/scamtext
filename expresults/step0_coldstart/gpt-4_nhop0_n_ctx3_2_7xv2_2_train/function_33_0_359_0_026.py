import re

def is_spam(text):
    spam_keywords = ['증권', '거래량', '상승', '하락', '공시', '투자', '광고', '발표', '수신거부', '최소', '상한가']
    urls = re.findall('https?://(?:[-\w.]|(?:%[\da-fA-F]{2}))+', text) + re.findall('(?:[-\w.]|(?:%[\da-fA-F]{2}))+\.[a-zA-Z0-9]+', text)

    if urls and any(keyword in text for keyword in spam_keywords):
        return True
        
    return False