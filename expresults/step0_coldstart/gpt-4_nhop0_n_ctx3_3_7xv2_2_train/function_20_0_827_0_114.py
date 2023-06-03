
import re

def is_spam(text):
    # List of spam-related keywords
    spam_keywords = ['만원', '폭등', '아줌마', '오픈초대', '해선', '단체방', '공개', '매집', '관련주', '비용요구', '정보만', '올바른 선택']
    
    # Regular expressions to identify spam patterns
    url_pattern = re.compile(r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\\(\\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+')
    korean_url_pattern = re.compile(r'(http|https)://(www\.)?[ㄱ-ㅎ가-힣A-Za-z0-9-_]+\s?\.co\s?\.kr')
    phone_pattern = re.compile(r'(\(?(\d{2,3}\))?[\s\.-](\d{1,6}[\s\.-]{0,1}\d{2,}[\s\.-]\d{2,}|\d{2,})|(\(\d{2,}\)|\d{2,})[\s\.-]\d{1,6}[\s\.-]\d{4})')
    
    # Count the number of spam-related keywords
    keyword_count = sum([1 for keyword in spam_keywords if keyword in text])
    
    # Check if any spammy patterns are present
    has_url = bool(url_pattern.search(text) or korean_url_pattern.search(text))
    has_phone = bool(phone_pattern.search(text))

    # Classify as spam if multiple keywords are found or if any patterns are found
    return keyword_count > 1 or has_url or has_phone

