
import re

def is_spam(message):
    # Rule 1: Check for the presence of special characters or spaces between characters (common in spam messages)
    if re.search(r'[\W]', message):
        return True

    # Rule 2: Check for non-standard domain names
    domain_regex = r'(http|https)://[^\s/]+'
    domain_matches = re.findall(domain_regex, message)
    for match in domain_matches:
        if not ('.' in match and len(match) > 5):  # exclude standard ones
            return True

    # Rule 3: Check for unusual percentage signs
    if re.search(r'[%][^ ][^\d]', message):
        return True

    # Rule 4: Check for the presence of unusual substrings (광고, 보장, 무료, 무료거부, 등록, SMS, 입장, 1000명, 무조건, 매수)
    spam_keywords = ["광고", "보장", "무료", "무료거부", "등록", "SMS", "입장", "1000명", "무조건", "매수"]
    for word in spam_keywords:
        if word in message:
            return True

    return False
