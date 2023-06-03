
import re

def is_spam(message):
    spam_indicators = [
        r'\(광고\)',
        r'신년맞이 모집',
        r'무료거부',
        r'당첨 되셨습니다',
        r'아니다 싶으시면 나가셔도 좋습니다',
        r'단체방 관망하기',
        r'금일 하루만 입장가능합니다',
        r'\bvvip\b'
    ]

    for indicator in spam_indicators:
        if re.search(indicator, message, re.IGNORECASE):
            return True

    return False
