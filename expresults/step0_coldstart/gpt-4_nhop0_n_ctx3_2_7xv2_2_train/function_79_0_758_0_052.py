
import re

def is_spam(text):
    spam_patterns = [
        r'\d{6}',  # 6 consecutive digits
        r'\d+% 적중',  # Consecutive digits followed by % 적중
        r'https?:\/\/[^\s]+',  # URL
        r'최소\d배',  # 최소 followed by consecutive digits
        r'현재가대비',  # 현재가대비
        r'[▲▼]', # Triangle characters
        r'목표달성기념', # 목표달성기념
        r'\*+\s+', # Multiple * with spaces
    ]

    for pattern in spam_patterns:
        if re.search(pattern, text):
            return True
    return False
