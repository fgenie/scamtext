
import re

def is_spam(message: str) -> bool:
    # Check for url shorteners
    url_shorteners = ['me2.kr', 'gg.gg', 'kakaotalk.it', 'https:', '//', 'http:', 'opcn-kakao.com']
    for url_shortener in url_shorteners:
        if url_shortener in message:
            return True

    # Check for overuse of special characters
    special_chars_pattern = r'[^a-zA-Z0-9가-힣\s]'
    special_chars = re.findall(special_chars_pattern, message)
    if len(special_chars) / len(message) > 0.2:
        return True

    # Check for specific spam words/phrases
    spam_phrases = ['축하드립니다', '지금 폐/배터리 재생주', '포스코', '월체험반', '경제신문', '재생단지', '대형공시 발표확정', '주장코드', '부장출신들의 타점/분석', '나스닥', '지원금', '입장코드']
    for spam_phrase in spam_phrases:
        if spam_phrase in message:
            return True
           
    # If none of the spam conditions are met, return False (not spam)
    return False
