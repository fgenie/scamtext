
import re

def contains_url(text):
    url_pattern = re.compile(r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\\(\\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+')
    return bool(url_pattern.search(text))

def is_spam(text):
    text = text.lower()
    spam_keywords = ['구매', '성과', '상승', '추천주', '매집', '계약', '광고', '하세요', '링크', '상한가', '특징주', '체험반', '주식', '발표', '투자',
                    '공개', '운용', '법인증', '펀드', '운영', '인터넷뱅킹', '예정', '성장', '관리', '주가']
    
    if contains_url(text):
        for keyword in spam_keywords:
            if keyword in text:
                return True
    return False
