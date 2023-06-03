
import re


def is_spam(text):
    # Check for spam characteristics
    spam_indicators = [
        r"광고",
        r"\d+% ?\+ ?\d+%",
        r"\d일 무료",
        r"무료패키지",
        r"콤\d+",
        r"\(광고\)",
        r"무료거부",
        r"한개만 걸려라는"
    ]

    # Check for normal message characteristics
    normal_indicators = [
        r"신한카드",
        r"할인금액 안내",
        r"고객님",
        r"현대홈마트",
        r"전단행사",
        r"전단세일"
    ]

    for indicator in spam_indicators:
        if re.search(indicator, text):
            return True

    for indicator in normal_indicators:
        if re.search(indicator, text):
            return False

    return False
