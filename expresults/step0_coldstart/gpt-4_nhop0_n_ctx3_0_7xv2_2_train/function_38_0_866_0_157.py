
import re

def is_spam(message):
    message = message.lower()

    spam_indicators = [
        r'\d{2,}%\+',
        r'ma\d+\w+bbq',
        r'\d:\d',
        r't\.(?:ly|co)\/\w+',
        r'\d+\w',
        r'key:\d+',
        r'(무료)?거부\d+',
        r'\+\d{2,} %',
        r'(?:광고|ads?)'
    ]

    for indicator in spam_indicators:
        if re.search(indicator, message):
            return True

    normal_indicators = [
        r'배달 기사',
        r'강의',
    ]

    for indicator in normal_indicators:
        if re.search(indicator, message):
            return False

    return False
