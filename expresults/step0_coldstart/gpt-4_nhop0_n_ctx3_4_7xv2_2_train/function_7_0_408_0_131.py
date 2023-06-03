
import re

def is_spam(message):
    # Check for excessive use of special characters
    special_chars = re.findall(r'[-=+,#/\^$.@*\%!&\(\)]', message)
    if len(special_chars) / len(message) > 0.1:
        return True

    # Check for suspicious phrases and patterns in the message
    spam_phrases = ['상한가', '50% ↑', '인공지능', '시간이 지날 수록', '그린피']
    for phrase in spam_phrases:
        if phrase in message:
            return True

    # Check for consecutive repeated characters
    if re.search(r'(.)\1{3,}', message):
        return True

    # Check for suspicious URLs
    urls = re.findall(r'(https?://\S+)', message)
    for url in urls:
        if "ko.gl" in url or "opcn-kakao.com" in url:
            return True

    # If none of the spam rules apply, return False (i.e., message is not spam)
    return False
