
import re

def is_spam(text):
    spam_keywords = ['추천', '클릭', '보세요', '참여하기', '대응', '계실겁니다', '비용요구', '운영되는 차이점', '수익률', '성과', '무료수신거부', '광고']
    url_pattern = r'(https?:\/\/[^\s]+)|(opcn-kakao.com)|(me2.kr)|(han.gl)|(vo.la)|(bit.ly)|(openkakao.at)|(m.posk.kr)'
    excessive_exclamation_marks = r'(!\s*){3,}'

    if re.search(url_pattern, text) and any(keyword in text for keyword in spam_keywords):
        return True
    if re.search(excessive_exclamation_marks, text):
        return True
    return False
