
import re

def is_spam(text):
    # Check for common spam keywords
    spam_keywords = ['적중', '%', '이어서 오픈', '지 원 금', '승인전화', '입금 없어도', '무료거부', '상한가', '4월파이날', 'VIP', '성공지름길', '정확한 타점', '18일 긴급입수정보', '일만원으로', '1천만원만들기', '부자되기']
    
    # Check for url and phone number patterns
    url_pattern = re.compile(r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+')
    phone_number_pattern = re.compile(r'\d{2,4}-\d{2,4}-\d{4}')
    kb_code_pattern = re.compile(r'KBPay 바코드 결제 불가')
    
    # Check if any spam keyword or pattern is present in the text
    if any(keyword in text for keyword in spam_keywords) or url_pattern.search(text) or (phone_number_pattern.search(text) and not kb_code_pattern.search(text)):
        return True
    else:
        return False
