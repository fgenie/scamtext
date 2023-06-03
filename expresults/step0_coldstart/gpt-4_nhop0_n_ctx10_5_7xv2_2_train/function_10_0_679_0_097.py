
import re


def is_spam(message: str) -> bool:
    spam_keywords = [
        "수익", "적립금", "하루만", "카카오톡", "파이널", "광고", "특별찬스",
        "합병", "출발", "마감", "무료상담", "이벤트", "게임", "골드",
        "%↑", "안내", "실력입증", "추가종목", "마지막", "애로봇",
        "강요", "소외주", "메가", "검증", "종목상담", "하루",
        "타점", "분석", "능", "자전거부무", "광고", "☆"
    ]

    spam_numbers_pattern = [
        r"\d{2,}만원", r"\d+%"
    ]

    message = message.lower()

    for keyword in spam_keywords:
        if keyword in message:
            return True

    for pattern in spam_numbers_pattern:
        if re.search(pattern, message):
            return True

    return False
