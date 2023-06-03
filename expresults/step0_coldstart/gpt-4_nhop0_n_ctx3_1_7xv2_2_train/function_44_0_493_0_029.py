
import re

def is_spam(text):
    spam_words = ["목표달성", "수익률", "추천", "최소", "1위", "달성", "증권사", "펀드", "애널리스트", "종목", "개장전", "억대 수익", "20% 상승", "증권 tv", "실전투자대회", "TOP", "다차", "목표가", "익 절 가"]

    text = re.sub("[^가-힣0-9]+", " ", text).strip()
    for word in spam_words:
        if word in text:
            return True

    if re.search(r'\d{1,}\%', text):
        return True

    if 'https://' in text or 'http://' in text:
        domain = re.findall(r'http[s]?://([\w\d._]+)', text)
        for d in domain:
            if 'opcn-kakao.com' in d or 'han.gl' in d:
                return True

    return False
