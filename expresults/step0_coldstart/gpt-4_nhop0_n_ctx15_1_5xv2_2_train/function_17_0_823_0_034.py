
import re

def is_spam(message):
    spam_keywords = ["무료", "수익", "광고", "증.권", "안내", "금일부터", "최고급", "강의", "교육", "완료", "적립금", "확률", "세계", "비밀번호", "추천", "단체방", "오픈", "수익률", "매매", "마이크로", "내일부터", "리뉴얼"]

    regular_terms = ["안녕하세요", "넵", "감사합니다", "수고하세요", "좋은 하루 보내", "끝나고 뭐하냐?", "야야", "오늘", "안녕", "게임한판", "상황", "인터넷", "뱅킹", "계좌"]

    message = message.lower()

    spam_count = 0
    for keyword in spam_keywords:
        if keyword in message:
            spam_count += 1

    regular_count = 0
    for term in regular_terms:
        if term in message:
            regular_count += 1

    if re.search(r'https?://\S+', message) or re.search(r'\d{2}\.\d{2}%?', message):
        spam_count += 1

    if spam_count > regular_count:
        return True
    else:
        return False
