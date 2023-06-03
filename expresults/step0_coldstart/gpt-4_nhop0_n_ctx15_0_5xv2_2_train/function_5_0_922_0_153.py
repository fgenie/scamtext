
import re

def is_spam(message):
    patterns = [
        r'(비밀번호|광고|확인|혜택|수익|지원금|할인)',
        r'\d+\.?\d*%?',
        r'[a-zA-Z0-9]+\.kr|[a-zA-Z0-9]+\.com',
        r'https?\://[^\s]*',
        r'(월)\s*(수익)+',
        r'[가-힣]*([a-zA-Z0-9]*)(선물|추천종목|로또)+\s*[가-힣]*',
        r'(최저가|상한가)',
    ]

    detected_patterns = [re.search(pattern, message) for pattern in patterns]

    return any(detected_patterns)

