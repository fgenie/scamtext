
import re

def is_spam(message: str) -> bool:
    # Removing non-alphanumeric characters
    clean_message = re.sub(r'\W+', ' ', message.lower())

    # Keywords to detect spam messages
    spam_keywords = [
        "신고", "악의적인", "종료", "안내", "아줌마", "비밀", "폭등",
        "목표달성기념", "제공", "추천", "VIP", "수익", "투자", "초대",
        "방", "단체", "차별화", "바로가기", "신청", "원", "빠른", "루멘스",
        "커버", "디코딩", "08", "//", "광고", "선물", "교육",
        "무료거부", "입장", "실현", "수익률"
    ]

    for keyword in spam_keywords:
        if keyword in clean_message:
            return True

    return False
