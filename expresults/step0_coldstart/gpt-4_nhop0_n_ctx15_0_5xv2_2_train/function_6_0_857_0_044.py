
import re

def is_spam(message):
    # Pattern for typical spam keywords and URL formats
    spam_keywords = r'목표달성|추천|카톡방|회원님|VIP|투자|거래|증권|오픈|광고|종목|매집주|분석|수익|단타매매|성공지름길|무료거부|openkakao|han.gl|me2.kr'
    url_pattern = r'(?i)https?://(?:[-\w.]|(?:%[\da-fA-F]{2}))+'

    # Check if the keywords or URL pattern exists in the message
    if (re.search(spam_keywords, message) is not None) or (re.search(url_pattern, message) is not None):
        return True
    else:
        return False
