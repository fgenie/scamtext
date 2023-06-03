
import re

def is_spam(message):
    spam_indicators = [
        r"주+\s*[\d,]*원",
        r"[\d,]*원으로\s+[\d,]*원",
        r"백만원",
        r"https:[\S]*[A-Za-z]{2,4}|https?://[\S]*[A-Za-z]{2,4}",
        r"추천",
        r"다음타자",
        r"달성",
        r"편리한\s+자동진행",
        r"[\d]*,?[\d]*,?[\d]*원",
    ]

    for indicator in spam_indicators:
        if re.search(indicator, message):
            return True

    return False
