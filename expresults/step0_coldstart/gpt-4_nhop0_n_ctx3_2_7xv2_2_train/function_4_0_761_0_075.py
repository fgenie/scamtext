def is_spam(message: str) -> bool:
    import re

    spam_indicators = [
        r"\b클릭|신규정보|목표가|적중|주식|찬스|수익|손실\b",
        r"(\d+[%배])",
        r"\b(http|https)://\S+\b",
        r"\b[.,]+원",
    ]

    normal_indicators = [
        r"\b만나|주말|뭐해|보냈다\b",
    ]

    spam_points = sum([bool(re.search(pattern, message)) for pattern in spam_indicators])
    normal_points = sum([bool(re.search(pattern, message)) for pattern in normal_indicators])

    if spam_points > normal_points:
        return True
    return False