
import re

def is_spam(message):
    message = message.lower()

    spam_indicators = [
        "\d배 이상 적중",
        "액톡방",
        "목표가:",
        "순위 정보 공유",
        "작전정보",
        "거래량 폭등",
        "신규정보",
        "카톡방 입장"
    ]

    normal_indicators = [
        "야 머하냐",
        "훈련",
        "보냈다"
    ]

    for indicator in spam_indicators:
        if re.search(indicator, message):
            return True

    for indicator in normal_indicators:
        if re.search(indicator, message):
            return False

    return False

