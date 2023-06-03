
import re

def is_spam(text: str) -> bool:
    # Check if there are URLs containing suspicious keywords
    url_pattern = re.compile(r'https?://\S+')
    suspicious_keywords = ["러", "텔레", "me2.kr", "han.gl", "dokdo.in", "vvd.bz"]
    urls = url_pattern.findall(text)
    for url in urls:
        if any(keyword in url for keyword in suspicious_keywords):
            return True

    # Check if there are words related to typical spam messages (money, gift, event, etc.)
    spam_pattern = re.compile(r'이벤트|혜택|종목|수익|성공|투자|프로젝트|게임|VIP|체험반|광고|MOU|$원칙|당첨')
    if spam_pattern.search(text):
        return True

    # Check if there are phrases like "100% win"
    win_rate_pattern = re.compile(r'\d{2,3}\s*전\s*\d{2,3}\s*승')
    if win_rate_pattern.search(text):
        return True

    # Check if there are suspicious number sequences
    suspicious_numbers = re.compile(r'계.약|4\d{4}|080\d{6,7}')
    if suspicious_numbers.search(text):
        return True

    return False
