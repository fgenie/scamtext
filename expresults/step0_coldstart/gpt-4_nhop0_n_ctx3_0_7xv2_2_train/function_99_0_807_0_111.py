
import re

def is_spam(message):
    # Check for common spam keywords such as promotions or ads
    spam_keywords = ["광고", "이벤트", "코드", "무료거부", "성과", "최근 성공현황", "bit.ly", "me2.kr"]

    # Check for unusual capitalization, as spammers tend to use capital letters more frequently
    upper_case_ratio = sum(1 for c in message if c.isupper()) / len(message)
    if upper_case_ratio > 0.3:
        return True

    # Check if the message has any of the spam keywords
    for keyword in spam_keywords:
        if keyword in message:
            return True

    # Check if the message contains multiple percent signs or currency symbols, which can indicate spam
    percent_sign_count = message.count('%')
    currency_count = message.count(',')

    if percent_sign_count > 1 or currency_count > 1:
        return True

    # Check for multiple consecutive digits, which can be an indication of spam
    multiple_digits_pattern = r"\d{3,}"
    if re.search(multiple_digits_pattern, message):
        return True

    # If the message passes all the checks, it's not spam
    return False
