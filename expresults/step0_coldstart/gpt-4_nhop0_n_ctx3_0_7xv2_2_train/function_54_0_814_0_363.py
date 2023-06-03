
import re

def is_spam(text):
    spam_indicators = [
        r"\d\w{2,}\s+[가-힣]\s*\d+(\s|%)+",
        r"\bSMS\s",
        r"안녕!",
        r"[!()\-?\[]+",
        r"://(?!openkakao)",
        r"[^\w]https?\S+",
        r"\d{6,}",
        r"\b선취매\b",
        r"\b수급\b",
        r"\b테마주\b",
        r"\b기술적 접근을 통한 단기 매매\b",
        r"\b수급과 재료를 통한 스윙 매매\b",
    ]

    for indicator in spam_indicators:
        if re.search(indicator, text):
            return True

    return False
