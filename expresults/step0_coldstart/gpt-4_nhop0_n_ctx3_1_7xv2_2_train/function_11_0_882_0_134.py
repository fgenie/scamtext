
import re

def is_spam(message):
    # Check for common spam characteristics
    spam_characteristics = [
        r'\d{2,5}',                 # multiple digits
        r'[가-힣]", "▼", "▲"',      # special characters
        r'(www\.)|(http)',         # URLs
        r'\b(원|목표가)\b',         # words related to stocks
        r'수.익', '유.료',           # spammy phrases
        r'(신약개발|분석|랙심|적인)', # spam-related words
        r'포인트 | 보기 | 전체메뉴 | 포인트 | 내 포인트' # spam phrases
        r'전문가, 실전투자대회 1위, 누적수익률', # expert claims
    ]
    
    for pattern in spam_characteristics:
        if re.search(pattern, message):
            return True
    return False
