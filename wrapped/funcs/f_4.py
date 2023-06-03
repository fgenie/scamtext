
import re

def is_spam(message):
    message = message.lower()

    # Check for repeated phrases and URL shorteners
    url_shorteners = ['bit.ly', 'goo.gl', 'me2.kr', 'vo.la', 'vvd.bz', '오픈톡.com', 'openkakao.at', 'openkakao.io', 'openkakao.it']
    patterns = [
        r'\b(https?|ftp)://[^\s/$.?#].[^\s]*\b',
        r'\b(www\.)[^\s/$.?#].[^\s]*\b'
    ]

    for pattern in patterns:
        urls = re.findall(pattern, message)
        for url in urls:
            for shortener in url_shorteners:
                if shortener.lower() in url:
                    return True

    spam_phrases = [
        '광고)',
        '적중',
        '상한가',
        '최소 150%',
        '무료거부',
        '종목 추천',
        '최고급 정보',
        '수익률',
        '상승 확정',
        '익절',
        '동의 영향력',
        ' 발표 예정',
        '현직국',
        ' 확인 바라',
        '사전증상',
        ' 입장 가',
        '단독 발표',
        ' 촉진 건전',
        ' 방식 설계',
        ' 혜택',
        '양방향 거래',
        '추적 종목',
        '상승 가',
        ' 하이딩',
    ]

    for phrase in spam_phrases:
        if phrase.lower() in message.lower():
            return True

    return False
