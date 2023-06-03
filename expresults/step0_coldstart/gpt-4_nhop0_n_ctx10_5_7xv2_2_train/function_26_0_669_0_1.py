
import re

def is_spam(text: str) -> bool:
    # Check for typical spam keywords and phrases
    spam_keywords = ["배터리 재생주", "입금 없어도", "출금", "광고", "신규 30,000원", "가입 없습니다", "무료거부", "아이션", "빠르고 정확한", "선물", "연속으로 외인", "2차전지", "최근 업급이 많은 테마주", "코드번호", "다른방과는 차원이 다른", "포항 2차전지 밸리내에 재생단지 건립중" ]
    for keyword in spam_keywords:
        if keyword in text:
            return True

    # Check for shortened URLs
    if re.search(r'(me2\.kr)|(t\.ly)|(orl\.kr)|(오픈톡\.com)', text):
        return True

    # Check for unusual punctuation
    if re.search(r'(!{2,})|(\*{2,})|(\.{3,})|(\(+)', text):
        return True

    # Check for phone numbers
    if re.search(r'\d{2,4}-\d{3,4}-\d{4}', text):
        return True
        
    return False
