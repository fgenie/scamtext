
import re

def is_spam(message):
    spam_keywords = [
        '광고', '만원지원', '지원받고', '지푸라기라도', '입장코드', '복리수익', '투자지원방', '나스닥', '수수료',
        '거부', '레퍼럴', '% 적중', '추천주', '지금 입장하세요'
    ]

    normal_keywords = [
        '하이', '안녕', '친구없음', '철수야'
    ]

    url_pattern = re.compile(r'https?:\/\/(?:[\w_-]+(?:(?:\.[\w_-]+)+))(?:[\w.,@?^=%&:/~+#-]*[\w@?^=%&/~+#-])?')

    message = re.sub(url_pattern, ' ', message)

    has_spam_keywords = any(keyword in message for keyword in spam_keywords)
    
    if not has_spam_keywords:
        return False

    has_normal_keywords = any(keyword in message for keyword in normal_keywords)

    if has_normal_keywords:
        return False

    return True
