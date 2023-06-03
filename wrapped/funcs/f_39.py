
import re

def is_spam(message):
    # Check for suspicious keywords
    spam_keywords = ["투자", "적중", " 아파트", "체험반", "상승", "광고", "지급", "방법", "수익", "더이상", "최근", "모두가"]
    for keyword in spam_keywords:
        if keyword in message:
            return True

    # Check for suspicious links
    suspicious_links = ["bit.ly", "me2.kr", "openkakao", "ko.gl"]
    for link in suspicious_links:
        if link in message:
            return True

    # Check for number patterns that might indicate a secret code, phone number or similar
    number_pattern = re.compile(r'\d{6,}|\d+(\,\d+)+|\d+(\.\d+)+')
    if number_pattern.search(message):
        return True

    # Check for excessive uses of special characters
    special_chars_pattern = re.compile(r'[\*\[\(\)!{}/■?%@Δ>▲|]')
    special_chars_count = len(special_chars_pattern.findall(message))
    if special_chars_count >= 3:
        return True

    return False
