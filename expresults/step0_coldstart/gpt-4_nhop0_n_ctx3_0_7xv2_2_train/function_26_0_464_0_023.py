
import re


def is_spam(text):
    # List of spam keywords
    spam_keywords = [
        "적중", "소니드", "수익률", "종목", "타점", "익절", "목표가", "미공개", "공시종목", "극비", "작전주",
        "VIP", "선정", "최소 금요일", "최소 금요일", "선착순 공개", "전문가", "경력"
    ]

    # Check for keywords
    for keyword in spam_keywords:
        if keyword in text:
            return True
    
    # Check for suspicious urls
    url_pattern = re.compile(r"https?://[^ ]+")
    urls = url_pattern.findall(text)

    for url in urls:
        if "spam_domain" in url:
            return True
    
    # check for phone numbers in the format of (06xxxxx) 
    phone_pattern = re.compile(r"\([0-9]{6}\)")
    phones = re.findall(phone_pattern, text)
    if phones:
        return True

    return False
