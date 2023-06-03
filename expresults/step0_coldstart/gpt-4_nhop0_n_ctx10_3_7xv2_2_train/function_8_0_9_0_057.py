
import re

def is_spam(message: str) -> bool:
    spam_words = [
        "증 권", "공시 종목", "언론에 나오기 전", "상승 확정", "익절", "수익률", "상한가",
        "단기", "테마주", "수급주", "무료체험반", "특별정보방", "거래량 폭등", "체험 기간",
        "수수료 율", "제세공과금", "로보마켓", "가입 혜택", "엔 계좌", "국 회의원",
        "해당 정보", "공시발표", "상한가달성", "청개구리", "첫 금액", "지원금", "노하우",
        "유니온", "언론사 미공개","입장", "클릭", "탈주"
    ]

    message = message.lower()

    for word in spam_words:
        if word in message:
            return True

    url_pattern = r"(http(s)?://)?(\w+\.)+\w{2,10}"

    if re.search(url_pattern, message):
        return True

    return False
