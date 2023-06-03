
import re

def is_spam(text):
    # Check for unusual numeric or special characters percentage
    non_alphabetic_chars = sum(not c.isalnum() for c in text)
    percentage = non_alphabetic_chars / len(text)
    if percentage > 0.3:
        return True

    # Check for excessively long alphanumeric strings (potential URLs)
    alphanumeric_chunks = re.compile(r'\S+').split(text)
    for chunk in alphanumeric_chunks:
        if len(chunk) > 20:
            return True

    # Check for common spam phrases
    spam_phrases = ['상한가', '최고이자율', '특별정보', 'M반도체', '적금', '출금', '출시', '이벤트', 
                    '공개', '혜택', '우대', '핵심정보', '투자', '수익률', '계좌']
    for phrase in spam_phrases:
        if phrase in text:
            return True

    return False
