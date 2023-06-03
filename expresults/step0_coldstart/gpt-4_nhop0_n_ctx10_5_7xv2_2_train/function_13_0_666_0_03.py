
import re

def is_spam(text):
    # Check the message for multiple links, which indicates spam
    links = re.findall("https?://[^\s]+", text)
    if len(links) > 1:
        return True

    # Check the message for typical spammy words or phrases
    spammy_words = ['상한가', '즉시할인', '여의도', '체험반', '광고', '알려드린', '축하합니다', '상승세', '이익', '비밀번호', '무료거부', '추천종목', '투자반',
                    '져지난', '프로필', '트레이딩', '시장의 경기', '진입하시길', '열심히', '안전한 투자', '거래대금']
    for word in spammy_words:
        if word in text:
            return True

    # Check if the message contains any suspicious short links
    short_links = re.findall("http(s)?://(me2\.kr|hani\.gl|asq\.kr|t\.ly|bit\.ly)/[^\s]+", text)
    if short_links:
        return True

    # If none of the above conditions apply, the message is likely normal
    return False
