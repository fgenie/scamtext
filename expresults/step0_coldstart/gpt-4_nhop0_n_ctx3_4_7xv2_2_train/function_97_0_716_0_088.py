
import re

def is_spam(text):
    # Check for signs indicating spam messages
    spam_indicators = [
        r"^\((.*)\)",
        r"\b(성공지름길|정확한 타점)\b",
        r"\bhttps?://[.\w]+(/[\w]+)?\b",
        r"\b[0-9]{4,}\b",
        r"\b(무료거부|거부|장문금지|수신자명단거부|광고사전지급)\b",
        r"\b웹에>|지>신규|카>[a-z0-9]\w+\b",
        r"\b(예금|대출|금리|이자)[\s]*[업무]*[\s]*",
        r"\b(신규\[이벤트\]|신한카드|만료되다|가입하다|[가방|모바일과장]\s*[제휴]?)\b",
    ]

    for indicator in spam_indicators:
        if re.search(indicator, text, re.IGNORECASE):
            return True

    return False
