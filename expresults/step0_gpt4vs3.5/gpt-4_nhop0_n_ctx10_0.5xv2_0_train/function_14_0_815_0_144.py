def is_spam(message):
    import re

    # Check for common spam text patterns
    spam_patterns = [
        r"(?i)(vip|폭등|비밀|공시|공개|오픈초대|오픈|체험반|추천|목표가|해선|단체방)",
        r"(?i)(연락|축하드립니다|클릭|무료입장|누적수익률)",
        r"(\d{1,3}[,.]?\d{0,3}[,.]?\d{0,3}원)",  # Monetary amounts
        r"(\d{1,2}일추천)",
        r"(?i)(증권|증권사|차별화된|금전적인 요구|스톡|종목|재테크|공시|투자|시세|주식)",
        r"((?:https?|ftp)://[^\s/$.?#]*.[^\s]*)",  # URLs
    ]

    for pattern in spam_patterns:
        if re.search(pattern, message):
            return True

    return False