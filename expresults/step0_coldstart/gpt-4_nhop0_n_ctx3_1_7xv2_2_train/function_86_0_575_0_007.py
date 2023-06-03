
import re

def is_spam(text):
    # Check for common spam phrases
    spam_phrases = [
        "목표달성기념",
        "추가종목",
        "디젠스",
        "VIP투자반",
        "무 료 체 험",
        "자 동 매 매"
    ]
    
    for phrase in spam_phrases:
        if phrase in text:
            return True

    # Check for excessive use of special characters
    special_characters = ['*', '^', '▼', '▲']
    special_count = sum(text.count(char) for char in special_characters)
    if special_count >= 3:
        return True

    # Check for suspicious URL patterns
    if re.search(r'https?://(?:[a-z0-9]|[A-Z])+(?:\.kr|\.gl)', text):
        return True

    return False
