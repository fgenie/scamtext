
import re

def is_spam(message):
    # Spam indicators
    spam_indicators = [
        r"[\d,]*원",
        r"\d{1,2}% ?~",
        r"\d{1,2}대",
        r"http[s]?://",
        r"주식",
        r"종목",
        r"익 절 가",
        r"펀드매니저",
        r"수익률",
        r"매매승률",
        r"목표가",
        r"최소",
        r"매일",
        r"최대",
        r"최고",
    ]

    # Iterate through spam indicators and check if any are present in the message
    for indicator in spam_indicators:
        if re.search(indicator, message, flags=re.IGNORECASE):
            return True

    # If none of the spam indicators are present, consider it a normal message
    return False
