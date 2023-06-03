
import re

def is_spam(text):
    # Check for common spam phrases and symbols
    spam_phrases = [
        "무료거부",
        "◆",
        "★"
    ]
    for phrase in spam_phrases:
        if phrase in text:
            return True

    # Check for unusual links
    unusual_links = [
        "me2.kr",
        "abit.ly",
        "fastkakao.com",
        "openkakao.at"
    ]
    for link in unusual_links:
        if link in text:
            return True

    # Check for unusual amount of numbers or percentages
    if len(re.findall(r'\d+%', text)) > 3 or len(re.findall(r'\d+', text)) > 10:
        return True

    return False
