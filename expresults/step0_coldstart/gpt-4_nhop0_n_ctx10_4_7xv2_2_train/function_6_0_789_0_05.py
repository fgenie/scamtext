
import re

def is_spam(text):
    spam_patterns = [
        r'\d{2}일',  # Dates like '18일'
        r'긴급입수',  # Emergency information
        r'상한가',  # Maximum price
        r'me2\.kr',  # Spam URLs
        r'기술특허',  # Technology patent
        r'https://[^ ]+',
        r'코드:',  # "Code"
        r'\(광고\)',  # Ads
        r'변할수',  # Change
        r'해선지원금',  # Support funds
        r'비밀번호 :',  # "Password"
        r'무료거부',  # "Free rejection"
        r'5만원',  # "50,000 won"
        r'신청',  # "Application"
        r'입장 안내',  # "Entrance guidance"
    ]

    for pattern in spam_patterns:
        if re.search(pattern, text):
            return True

    return False
