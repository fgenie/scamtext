
import re

def is_spam(message):
    spam_signals = [
        r"\d+\%{1}\s?[↑+]",
        r"bit\.ly",
        r"han\.gl",
        r"무료거부",
        r"코드\d+",
        r"공식발표확정",
        r"광고",
        r"\d일\d회",
        r"신I규l",
        r"1일300~",
    ]

    for pattern in spam_signals:
        if re.search(pattern, message):
            return True

    return False
