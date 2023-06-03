
import re

def is_spam(message: str) -> bool:
    # Check for phrases commonly found in spam messages
    spam_phrases = [
        '당첨 되셨습니다',
        '귀하의 투자계획은',
        '하락장',
        '수익',
        '연금 체계',
        '투자 방',
    ]

    # Check for suspicious URL patterns
    url_pattern = r'(https?://|[a-zA-Z0-9]+\.[a-zA-Z]{2,}/).+'

    # Check for excessive use of repeated words or characters
    repetition_pattern = r'(\b\w+\b).+\1'

    for phrase in spam_phrases:
        if phrase in message:
            return True

    if re.search(url_pattern, message) or re.search(repetition_pattern, message):
        return True

    return False
