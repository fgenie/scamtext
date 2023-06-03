
import re


def is_spam(text):
    # Check for common spam patterns
    if re.search(r'(비용요구|가입|무려|\d+\%\s*\+|상한가|수익확실|아이디|바카라|해선)', text):
        return True
    # Check for suspicious urls
    elif re.search(r'\b(?:https?|ftp)://\S+\b', text) and not re.search(r'\b(?:naver|google)\b', text):
        return False
    # Else consider it a normal message
    return False
