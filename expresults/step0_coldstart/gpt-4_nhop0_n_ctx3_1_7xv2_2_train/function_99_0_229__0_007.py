
import re

def is_spam(message: str) -> bool:
    keywords = ['축하합니다', '당첨', '추천주', '시황', '분석', '수익률', 'AI로봇사업', '상장스타트업', '계열사합병', '증권', '고급 정보', '매수세', '거래량', '폭등', '익절']
    url_pattern = re.compile(r'https?://[^\s]+') 
    shorten_url_pattern = re.compile(r'\bme2\.kr/[^\s]+')
    kakao_url_pattern = re.compile(r'\bopenkakao\.io/[^\s]+')
    
    if url_pattern.search(message) or shorten_url_pattern.search(message) or kakao_url_pattern.search(message):
        if any(keyword in message for keyword in keywords):
            return True

    return False
