
import re

def is_spam(text: str) -> bool:
    
    keywords = [
        '광고', '금전요구', '2차전지', '투자증권', '카톡방', '주식계좌',
        '최근 투자', '지식이 아닙니다', '단 1원', '약속드립니다',
        '선착순', '무료거부', '연혁', '차별화된 정보'
    ]
    
    if any(keyword in text for keyword in keywords):
        return True
    
    bitly_links = re.findall(r"bit\.ly/\w+", text)
    me2_links = re.findall(r"me2\.kr/\w+", text)
    
    if len(bitly_links) + len(me2_links) >= 2:
        return True
    
    return False
