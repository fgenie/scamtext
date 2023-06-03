
import re

def is_spam(message):
    # Checking for typical spam words and phrases
    spam_phrases = ["광고", "에스비비테크", "케이사인", "slot", "zone", "무료수신거부", "처음혜택", "코/드", "첫%d", "첫 %", "매 %", "abit", "페백"]
    for phrase in spam_phrases:
        if phrase in message:
            return True
    
    # Checking for URL shorteners, which are commonly used in spam messages
    short_url_patterns = [r"bit\.ly", r"a\.to", r"ⓢlⓩ"]
    for pattern in short_url_patterns:
        if re.search(pattern, message):
            return True

    # Checking for sequences of special characters
    special_char_pattern = r"[^A-Za-z가-힣ㄱ-ㅎㅏ-ㅣ0-9\s]+"
    matches = re.findall(special_char_pattern, message)
    for match in matches:
        if len(match) > 1:
            return True

    return False
