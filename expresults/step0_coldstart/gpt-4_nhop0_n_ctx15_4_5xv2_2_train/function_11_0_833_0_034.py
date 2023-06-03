
import re

def is_spam(message):
    # Check for common spam indicators
    spam_indicators = [
        r"(광고)",  # 광고 keyword
        r"(추천종목)",  # 추천종목 keyword
        r"\bh.t.t.p.s?:\/\/\S*",  # shortened urls
        r"([A-Za-z0-9]{3,}(\.[A-Za-z0-9]{2,})+)\/?[A-Za-z0-9]*\b",  # urls with no http(s)
        r"▒+",  # multiple consecutive square characters
        r"♥+",  # multiple consecutive heart characters
        r"▲+",  # multiple consecutive triangle characters
        r"※",  # reference mark character
        r"(.{2,40}\s?\|)",  # '|' character within 40 characters from start of the line
        r"[0-9]{2,}[,.\s]*[0-9]{4,}",  # numbers separated by comma or space
        r"월공개",
        r"무료.+거부",  # 무료 followed later by 거부
    ]
    
    # Check the presence of each of the above spam-related patterns
    for indicator in spam_indicators:
        if re.search(indicator, message):
            return True
    
    # If none of the above patterns are found, the message is not spam
    return False
