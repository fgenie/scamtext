
import re

def is_spam(text):
    spam_keywords = ['목표달성기념', '추천', '퍼.센.트▲', '참여하기', '매집단계', '상태', '좋은 선택', '문의주세요', '무료수신거부']
    special_chars = re.compile(r'[▼▶▲]')

    # Check for special characters
    if special_chars.search(text):
        return True

    # Check for long sequences of the same character
    if re.search(r'(.)\1{5,}', text):
        return True

    # Check for spam keywords
    for keyword in spam_keywords:
        if keyword in text:
            return True

    return False
