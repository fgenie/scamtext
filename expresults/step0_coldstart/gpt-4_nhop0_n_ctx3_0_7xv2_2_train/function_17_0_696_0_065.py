def is_spam(message: str) -> bool:
    import re

    # Check for suspicious words or phrases
    spam_keywords = ["상한가", "환급", "공시정보", "이벤트 이메일"]
    for keyword in spam_keywords:
        if keyword in message:
            return True

    # Check for suspicious URL shorteners
    shorteners = ["ko.gl", "me2.kr"]
    for shortener in shorteners:
        if shortener in message:
            return True

    # Check for a high number of won or other currency
    won_found = re.search(r"([1-9]\d*,?\d{0,2}0{4,}원|(\$|#|￥|€|£)?( ){0,1}[1-9]\d{0,2},?\d{0,2}0{2,})", message)
    if won_found:
        return True

    # Otherwise, it is not spam
    return False