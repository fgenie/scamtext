
import re

def is_spam(message: str) -> bool:
    # Check for common spam phrases and patterns
    spam_phrases = [
        '특별', '상승', '배당', '파이널', '금일', '최대', '무료', 'VIP', '차별화', '종목', '시작', '추천주', '단독입수', '단타', '매매', '건설', '수익', '어째', '정보',
        '관심종목', '참고로', '희망', '여행관련주', '가상화폐', '털보임',
        '정상적인 문자형식',
        '교수의', '국제유가',
        '원칙입니다.',
        '도운',
        '한농화성',
        '여행주가',
    ]

    # Check for URL shortening services
    url_shorteners = [
        'https://tuney.kr', 'http://bit.ly', 'https://me2.kr', 'https://vvd.bz', 'https://bit.ly', 'https://ls38.xyz', 'https://0xf.kr', 'https://tr.im'
    ]

    # Check for excessive special characters
    special_char_pattern = r'[!@#$%^&*()-_=+[\]{}/?.,;:]+'

    if any(spam_phrase in message for spam_phrase in spam_phrases):
        return True
    if any(url_shortener in message for url_shortener in url_shorteners):
        return True
    if len(re.findall(special_char_pattern, message)) > 4:
        return True

    return False
