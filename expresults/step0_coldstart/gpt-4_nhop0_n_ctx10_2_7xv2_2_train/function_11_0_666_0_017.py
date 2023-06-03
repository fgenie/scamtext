
import re

def is_spam(message):
    spam_keywords = [
        "최소3연상", "미리확인", "상한가", "급등예정", "체험반", " 수익", "단독입수",
        "적중", "단체방", "운영", "발표", "무료수신거부", "누적수익", "특별공유",
        "연속 당첨", "유튜브 경제야 놀자", "VIP단톡방", "익명확보", "특징주공개"
    ]
    spam_url_patterns = [
        r"https?://me2\.kr", r"https?://han\.gl", r"https?://abit\.ly",
        r"https?://bit\.ly", r"https?://vvd\.bz", r"https?://openkakao\.it"
    ]

    if any(keyword in message for keyword in spam_keywords):
        return True

    for pattern in spam_url_patterns:
        if re.search(pattern, message):
            return True

    return False
