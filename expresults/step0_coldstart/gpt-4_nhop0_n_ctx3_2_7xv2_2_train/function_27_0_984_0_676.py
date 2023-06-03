
import re

def is_spam(message):
    # Check for non-standard ASCII characters
    non_ascii_chars = re.findall(r'[^\x00-\x7F]', message)
    if len(non_ascii_chars) > 5:
        return True

    # Check for common spam words
    spam_words = ["신용", "카지노", "승인", "대출", "보험", "홍보", "매출", "확인", "이벤트", "추천", "쿠폰", "프로모션", "할인", "정품", "당첨", "배달", "대행", "무료", "바로가기", "간편하게", "상품", "오픈", "링크", "예약", "결제", "소개"]
    for word in spam_words:
        if word in message:
            return True

    # Check for URL patterns
    urls = re.findall(r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\\(\\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', message)
    if len(urls) > 0:
        return True

    return False
