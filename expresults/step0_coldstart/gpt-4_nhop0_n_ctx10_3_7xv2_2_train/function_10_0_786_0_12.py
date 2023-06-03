
import re

def is_spam(text: str) -> bool:
    spam_keywords = ['광고', '매수', '매수매도타점', '성과', '조각구매', '차익방법', '수혜주', '사업', '알고계신가요', '공시발표', '상품 목록', '약속']
    url_pattern = r'https?://\S+|bit\.ly/\S+|me2\.kr/\S+|[\w.]*?kakao\.io/\S+'
    consecutive_special_chars = r'([!?.]){2,}'

    is_spam = False

    # Check if the text has spam keywords, urls, or consecutive_special_chars
    if any(keyword in text for keyword in spam_keywords) or re.search(url_pattern, text) or re.search(consecutive_special_chars, text):
        is_spam = True

    return is_spam
